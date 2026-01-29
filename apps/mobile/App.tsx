import React, { useMemo, useState } from "react";
import { SafeAreaView, Text, View, Pressable, ScrollView } from "react-native";
import * as Speech from "expo-speech";

type DailySession = {
  mission: string;
  scene: string;
  tone: "formal" | "casual";
  sentences: Array<{
    pl: string;
    sv: string;
    checks?: Array<{ q: string; a: string }>;
  }>;
  dialog_seed: { role: string; opening: string };
  patterns?: Array<{ template: string; examples: string[] }>;
  start_srs?: Array<{ front: string; back: string; tags: string[] }>;
};

type DailySessionRecord = {
  id: string;
  session_date: string;
  session_json: DailySession;
};

const API_BASE = process.env.EXPO_PUBLIC_API_BASE ?? "http://localhost:8000";

export default function App() {
  const [session, setSession] = useState<DailySessionRecord | null>(null);
  const [error, setError] = useState<string | null>(null);

  const dailySession = session?.session_json;
  const firstSentence = useMemo(
    () => dailySession?.sentences?.[0],
    [dailySession]
  );

  async function loadToday() {
    setError(null);
    try {
      const res = await fetch(`${API_BASE}/v1/daily-session?scenario=cafe&tone=formal`);
      if (!res.ok) throw new Error(`API error: ${res.status}`);
      const json = (await res.json()) as DailySessionRecord;
      setSession(json);
    } catch (e: any) {
      setError(e?.message ?? "Unknown error");
    }
  }

  function speakPL() {
    if (!firstSentence?.pl) return;
    Speech.speak(firstSentence.pl, { language: "pl-PL" });
  }

  return (
    <SafeAreaView style={{ flex: 1, padding: 16 }}>
      <Text style={{ fontSize: 24, fontWeight: "600" }}>Lingo</Text>
      <Text style={{ marginTop: 6, opacity: 0.8 }}>
        Dagens scenkort + snabb feedback.
      </Text>

      <View style={{ height: 12 }} />

      <Pressable
        onPress={loadToday}
        style={{ backgroundColor: "#111", padding: 12, borderRadius: 10 }}
      >
        <Text style={{ color: "#fff", fontWeight: "600" }}>Hämta dagens pass</Text>
      </Pressable>

      {error ? (
        <Text style={{ marginTop: 12, color: "#b00020" }}>{error}</Text>
      ) : null}

      <ScrollView style={{ marginTop: 12 }}>
        {dailySession ? (
          <View style={{ gap: 12 }}>
            <View
              style={{
                backgroundColor: "#f6f6f6",
                borderRadius: 16,
                padding: 16,
                gap: 12,
              }}
            >
              <View
                style={{
                  height: 180,
                  borderRadius: 12,
                  backgroundColor: "#ddd",
                  alignItems: "center",
                  justifyContent: "center",
                }}
              >
                <Text style={{ opacity: 0.6 }}>Bild kommer här</Text>
              </View>

              <View style={{ gap: 4 }}>
                <Text style={{ fontSize: 18, fontWeight: "600" }}>
                  {dailySession.mission}
                </Text>
                <Text style={{ opacity: 0.8 }}>
                  {dailySession.scene} · {dailySession.tone}
                </Text>
              </View>

              <View style={{ gap: 6 }}>
                <Text style={{ fontSize: 16, fontWeight: "600" }}>
                  Dagens fras
                </Text>
                <Text style={{ fontSize: 18 }}>{firstSentence?.pl}</Text>
                <Text style={{ opacity: 0.75 }}>{firstSentence?.sv}</Text>
              </View>

              <View style={{ flexDirection: "row", gap: 10 }}>
                <Pressable
                  onPress={speakPL}
                  style={{
                    flex: 1,
                    backgroundColor: "#111",
                    padding: 12,
                    borderRadius: 10,
                    alignItems: "center",
                  }}
                >
                  <Text style={{ color: "#fff", fontWeight: "600" }}>Spela</Text>
                </Pressable>
                <View
                  style={{
                    flex: 1,
                    backgroundColor: "#ececec",
                    padding: 12,
                    borderRadius: 10,
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <Text style={{ fontWeight: "600" }}>Säg det</Text>
                  <Text style={{ fontSize: 12, opacity: 0.6 }}>(kommer snart)</Text>
                </View>
              </View>
            </View>

            <View style={{ gap: 8 }}>
              <Text style={{ fontSize: 16, fontWeight: "600" }}>
                Snabb feedback
              </Text>
              <View style={{ flexDirection: "row", gap: 8 }}>
                {["Lätt", "OK", "Svårt"].map((label) => (
                  <View
                    key={label}
                    style={{
                      flex: 1,
                      paddingVertical: 10,
                      borderRadius: 999,
                      backgroundColor: "#f1f1f1",
                      alignItems: "center",
                    }}
                  >
                    <Text style={{ fontWeight: "600" }}>{label}</Text>
                  </View>
                ))}
              </View>
            </View>

            {firstSentence?.checks?.length ? (
              <View style={{ gap: 6 }}>
                <Text style={{ fontSize: 16, fontWeight: "600" }}>
                  Förståelsekoll
                </Text>
                {firstSentence.checks.map((check, index) => (
                  <View key={`${check.q}-${index}`} style={{ gap: 2 }}>
                    <Text>• {check.q}</Text>
                    <Text style={{ opacity: 0.8 }}>Svar: {check.a}</Text>
                  </View>
                ))}
              </View>
            ) : null}

            <View style={{ gap: 4 }}>
              <Text style={{ fontSize: 16, fontWeight: "600" }}>Dialog-start</Text>
              <Text style={{ opacity: 0.8 }}>{dailySession.dialog_seed.role}</Text>
              <Text>{dailySession.dialog_seed.opening}</Text>
            </View>

            {dailySession.patterns?.length ? (
              <View style={{ gap: 6 }}>
                <Text style={{ fontSize: 16, fontWeight: "600" }}>Mönster</Text>
                {dailySession.patterns.map((pattern, index) => (
                  <View key={`${pattern.template}-${index}`} style={{ gap: 2 }}>
                    <Text>{pattern.template}</Text>
                    <Text style={{ opacity: 0.8 }}>
                      Exempel: {pattern.examples.join(" ")}
                    </Text>
                  </View>
                ))}
              </View>
            ) : null}
          </View>
        ) : (
          <Text style={{ marginTop: 12, opacity: 0.7 }}>
            Ingen session laddad ännu.
          </Text>
        )}
      </ScrollView>
    </SafeAreaView>
  );
}
