import React, { useMemo, useState } from "react";
import { SafeAreaView, Text, View, Pressable, ScrollView } from "react-native";
import * as Speech from "expo-speech";

// MVP: minimal UI to prove the loop: fetch a DailySession JSON and play TTS.
// Later: replace with proper navigation + Scene Card UI.

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
};

const API_BASE = process.env.EXPO_PUBLIC_API_BASE ?? "http://localhost:8000";

export default function App() {
  const [session, setSession] = useState<DailySession | null>(null);
  const [error, setError] = useState<string | null>(null);

  const firstSentence = useMemo(() => session?.sentences?.[0], [session]);

  async function loadToday() {
    setError(null);
    try {
      const res = await fetch(`${API_BASE}/v1/daily-session`);
      if (!res.ok) throw new Error(`API error: ${res.status}`);
      const json = (await res.json()) as DailySession;
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
      <Text style={{ fontSize: 24, fontWeight: "600" }}>Lingo (MVP)</Text>
      <Text style={{ marginTop: 6, opacity: 0.8 }}>
        Proof-of-loop: hämta dagens JSON och spela upp första PL-meningen med TTS.
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
        {session ? (
          <View style={{ gap: 10 }}>
            <Text style={{ fontSize: 16, fontWeight: "600" }}>Mission</Text>
            <Text>{session.mission}</Text>

            <Text style={{ fontSize: 16, fontWeight: "600" }}>Scenario</Text>
            <Text>
              {session.scene} · {session.tone}
            </Text>

            <Text style={{ fontSize: 16, fontWeight: "600" }}>Mening #1</Text>
            <Text style={{ fontSize: 18 }}>{firstSentence?.pl}</Text>
            <Text style={{ opacity: 0.8 }}>{firstSentence?.sv}</Text>

            <Pressable
              onPress={speakPL}
              style={{ backgroundColor: "#eee", padding: 12, borderRadius: 10 }}
            >
              <Text style={{ fontWeight: "600" }}>Lyssna (TTS)</Text>
            </Pressable>

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
              <Text style={{ opacity: 0.8 }}>{session.dialog_seed.role}</Text>
              <Text>{session.dialog_seed.opening}</Text>
            </View>

            {session.patterns?.length ? (
              <View style={{ gap: 6 }}>
                <Text style={{ fontSize: 16, fontWeight: "600" }}>Mönster</Text>
                {session.patterns.map((pattern, index) => (
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
          <Text style={{ marginTop: 12, opacity: 0.7 }}>Ingen session laddad ännu.</Text>
        )}
      </ScrollView>
    </SafeAreaView>
  );
}
