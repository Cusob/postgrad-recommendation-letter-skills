# 状态接口

位置：当前工作区 `.postgrad-recommendation-letter/profile.json`。

入口 skill 写入；执行 skill 只读。

```json
{
  "schema_version": 1,
  "status": "initialized",
  "initialized_at": "ISO-8601 timestamp",
  "updated_at": "ISO-8601 timestamp",
  "resume": {
    "path": "path",
    "sha256": "hex digest",
    "file_type": "pdf|docx|other",
    "readable": true,
    "read_at": "ISO-8601 timestamp"
  },
  "profile": {
    "identity": {},
    "education": [],
    "academics": {},
    "research": [],
    "engineering": [],
    "awards": [],
    "skills": [],
    "preferences": {},
    "unknowns": []
  },
  "profile_sources": [],
  "template": {
    "mode": "uploaded|default",
    "path": "path or null",
    "sha256": "hex digest or null",
    "format": "docx|other|default-docx",
    "origin": "user-uploaded|default|user-accepted-draft",
    "accepted_at": "ISO-8601 timestamp or null",
    "contract": {
      "preserve": [],
      "adapt": [],
      "discard": []
    },
    "default_version": "version or null"
  }
}
```

导师、论文、任务产物和 QA 不写入长期个人状态。
