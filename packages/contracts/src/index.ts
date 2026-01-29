import { z } from "zod";

export const ToneSchema = z.enum(["formal", "casual"]);

export const CheckSchema = z.object({
  q: z.string().min(1),
  a: z.string().min(1)
});

export type Check = z.infer<typeof CheckSchema>;

export const SentenceSchema = z.object({
  pl: z.string().min(1),
  sv: z.string().min(1),
  checks: z.array(CheckSchema).min(1).optional()
});

export type Sentence = z.infer<typeof SentenceSchema>;

export const DialogSeedSchema = z.object({
  role: z.string().min(1),
  opening: z.string().min(1)
});

export type DialogSeed = z.infer<typeof DialogSeedSchema>;

export const PatternSchema = z.object({
  template: z.string().min(1),
  examples: z.array(z.string().min(1)).min(1)
});

export type Pattern = z.infer<typeof PatternSchema>;

export const DailySessionSchema = z.object({
  mission: z.string().min(1),
  scene: z.string().min(1),
  tone: ToneSchema,
  sentences: z.array(SentenceSchema).min(1),
  dialog_seed: DialogSeedSchema,
  patterns: z.array(PatternSchema).optional()
});

export type DailySession = z.infer<typeof DailySessionSchema>;

export const DailySessionJsonSchema = {
  $schema: "http://json-schema.org/draft-07/schema#",
  title: "DailySession",
  type: "object",
  properties: {
    mission: { type: "string", minLength: 1 },
    scene: { type: "string", minLength: 1 },
    tone: { type: "string", enum: ["formal", "casual"] },
    sentences: {
      type: "array",
      minItems: 1,
      items: {
        type: "object",
        properties: {
          pl: { type: "string", minLength: 1 },
          sv: { type: "string", minLength: 1 },
          checks: {
            type: "array",
            minItems: 1,
            items: {
              type: "object",
              properties: {
                q: { type: "string", minLength: 1 },
                a: { type: "string", minLength: 1 }
              },
              required: ["q", "a"]
            }
          }
        },
        required: ["pl", "sv"]
      }
    },
    dialog_seed: {
      type: "object",
      properties: {
        role: { type: "string", minLength: 1 },
        opening: { type: "string", minLength: 1 }
      },
      required: ["role", "opening"]
    },
    patterns: {
      type: "array",
      items: {
        type: "object",
        properties: {
          template: { type: "string", minLength: 1 },
          examples: {
            type: "array",
            minItems: 1,
            items: { type: "string", minLength: 1 }
          }
        },
        required: ["template", "examples"]
      }
    }
  },
  required: ["mission", "scene", "tone", "sentences", "dialog_seed"]
} as const;
