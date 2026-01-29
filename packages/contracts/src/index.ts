import { z } from "zod";

export const ToneSchema = z.enum(["formal", "casual"]);

export const CheckSchema = z.object({
  q: z.string().min(1),
  a: z.string().min(1)
});

export const SentenceSchema = z.object({
  pl: z.string().min(1),
  sv: z.string().min(1),
  checks: z.array(CheckSchema).min(1).optional()
});

export const DialogSeedSchema = z.object({
  role: z.string().min(1),
  opening: z.string().min(1)
});

export const PatternSchema = z.object({
  template: z.string().min(1),
  examples: z.array(z.string().min(1)).min(1)
});

export const DailySessionSchema = z.object({
  mission: z.string().min(1),
  scene: z.string().min(1),
  tone: ToneSchema,
  sentences: z.array(SentenceSchema).min(1),
  dialog_seed: DialogSeedSchema,
  patterns: z.array(PatternSchema).optional()
});

export type DailySession = z.infer<typeof DailySessionSchema>;
