# Contoh struktur data survey
survey = {
    "Survey_A": [
        {"trace_id": 1, "QC_flag": "GOOD", "receiver": "R1"},
        {"trace_id": 2, "QC_flag": "BAD", "receiver": "R2"},
    ],
    "Survey_B": [
        {"trace_id": 3, "QC_flag": "GOOD", "receiver": "R1"},
        {"trace_id": 4, "QC_flag": "BAD", "receiver": "R3"},
        {"trace_id": 5, "QC_flag": "GOOD", "receiver": "R2"},
    ],
    "Survey_C": [
        {"trace_id": 6, "QC_flag": "BAD", "receiver": "R1"},
    ]
}

# 1. Cari trace BAD
trace_bad = [trace["trace_id"] for daftar_trace in survey.values() for trace in daftar_trace if trace["QC_flag"] == "BAD"]

# 2. Total trace
total_trace = sum(len(daftar_trace) for daftar_trace in survey.values())

# 3. Survey dengan trace terbanyak
survey_terbanyak = max(survey, key=lambda s: len(survey[s]))
bad_di_survey_terbanyak = sum(1 for trace in survey[survey_terbanyak] if trace["QC_flag"] == "BAD")

# 4. Receiver unik
receiver_unik = {trace["receiver"] for daftar_trace in survey.values() for trace in daftar_trace}

# 5. Jumlah trace per receiver
jumlah_receiver = {}
for daftar_trace in survey.values():
    for trace in daftar_trace:
        r = trace["receiver"]
        jumlah_receiver[r] = jumlah_receiver.get(r, 0) + 1

# === OUTPUT LAPORAN ===
print("=== Laporan Analisis Survey ===")
print("Total trace:", total_trace)
print("Total trace BAD:", len(trace_bad), "| ID:", trace_bad)
print("Survey dengan trace terbanyak:", survey_terbanyak, "(", len(survey[survey_terbanyak]), "trace )")
print("Jumlah trace BAD di survey tersebut:", bad_di_survey_terbanyak)
print("Receiver unik:", receiver_unik, "(", len(receiver_unik), "receiver )")
print("Jumlah trace per receiver:")
for r, jumlah in jumlah_receiver.items():
    print(f"- Receiver {r}: {jumlah} trace")
