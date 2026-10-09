# 状态接口

位置：当前工作区 `.postgrad-recommendation-letter/profile.json`。

入口 Skill 写入；执行 Skill 只读。旧 schema 状态在初始化 Skill 中向前迁移，不要求用户重复上传仍然有效的简历。

```json
{
  "schema_version": 3,
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
      "snapshot_path": "path or null",
      "snapshot_sha256": "hex digest or null",
      "generated_at": "ISO-8601 timestamp or null",
      "preserve": [
        "paragraph order and responsibilities",
        "tables, sections, headers, footers and media",
        "page margins and paragraph properties",
        "run-level styles unless a user-approved change is recorded"
      ],
      "adapt": [
        "personal facts that conflict with the resume",
        "old advisor, paper, direction and application target",
        "recognized placeholders and ordinary text with stale facts"
      ],
      "discard": [],
      "paragraph_map": [],
      "allowed_changes": []
    },
    "default_version": "version or null"
  }
}
```

导师、论文、任务产物和 QA 不写入长期个人状态。
