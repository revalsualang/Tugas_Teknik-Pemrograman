trace_bad = []
for survey_name, daftar_trace in survey.items():
    for trace in daftar_trace:
        if trace["QC_flag"] == "BAD"
            trace_bad.append(trace["trace_id"])
  
print("trace BAD:", trace_bad)