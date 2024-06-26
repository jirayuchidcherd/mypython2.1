std = {
    'name' : "Jirayu",
    "age":16,
    'gpa' :3.55,
    "old_sch" : "สาธิตสวนนัน"
    }

print(std)
print("สวัสดี %s" % std["name"])
print("อายุ %d เกรดเฉลี่ย %.2f  สาธิตสวนนัน %s " % (std["age"] , std["gpa"]  , std['gpa']))