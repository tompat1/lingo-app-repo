# DB-schema (Postgres / Supabase)

> Källa: användarens specifikation i denna kontext.

## UserProfile
```sql
create table user_profiles (
  user_id uuid primary key,
  goal text not null check (goal in ('travel','work','daily')),
  level text not null, -- A0..B2
  ui_language text not null default 'sv',
  target_language text not null default 'pl',
  tone_default text not null check (tone_default in ('formal','casual')),
  minutes_per_day int not null default 15,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
```

## Scenarios
```sql
create table scenarios (
  id text primary key, -- 'cafe', 'pharmacy'...
  name_sv text not null,
  tags text[] not null default '{}',
  created_at timestamptz not null default now()
);
```

## DailySession
```sql
create table daily_sessions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references user_profiles(user_id),
  session_date date not null,
  mission text not null,
  scenario_id text not null references scenarios(id),
  tone text not null check (tone in ('formal','casual')),
  session_json jsonb not null, -- renderbar AI-output
  created_at timestamptz not null default now(),
  unique (user_id, session_date)
);
```

## Attempt (audio/text)
```sql
create table attempts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references user_profiles(user_id),
  daily_session_id uuid references daily_sessions(id),
  input_type text not null check (input_type in ('audio','text')),
  stt_text text,
  target_text text,
  score jsonb, -- {match:..., fluency:...}
  created_at timestamptz not null default now()
);
```

## Mistakes
```sql
create table mistakes (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references user_profiles(user_id),
  daily_session_id uuid not null references daily_sessions(id),
  type text not null, -- 'politeness','vocab','case','word_order'...
  example jsonb not null, -- {user:"", corrected:"", note:""}
  fix jsonb, -- {pattern:"", tip:""}
  created_at timestamptz not null default now()
);
```

## SRS Cards
```sql
create table srs_cards (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references user_profiles(user_id),
  front text not null,
  back text not null,
  due_date date not null,
  ease numeric not null default 2.5,
  tags text[] not null default '{}',
  source text not null check (source in ('mistake','highfreq')),
  source_id uuid, -- optional: mistakes.id
  created_at timestamptz not null default now()
);

create index on srs_cards (user_id, due_date);
```

## Weekly Report
```sql
create table weekly_reports (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references user_profiles(user_id),
  week_start date not null,
  metrics jsonb not null,
  weaknesses jsonb not null,
  next_week_plan jsonb not null,
  created_at timestamptz not null default now(),
  unique (user_id, week_start)
);
```
