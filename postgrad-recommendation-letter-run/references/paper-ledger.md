# 候选论文证据账本模板

为每条候选论文保留一条记录。不要只保留最终选入正文的论文；替代、排除、同名待核验和全文获取失败的候选也保留，便于解释取舍并支持恢复。

```yaml
- title: ""
  authors: []
  year: null
  venue: ""
  doi_or_identifier: ""
  advisor_author_role: ""
  identity_confidence: "high|medium|low|unverified"
  identity_evidence: []
  research_stage: "early|core|transition|recent|unknown"
  research_line: ""
  representativeness: "core|important|supporting|uncertain"
  evidence_level: "PDF_FULLTEXT_READ|FULLTEXT_NON_PDF|ABSTRACT_ONLY|METADATA_ONLY|IDENTITY_UNVERIFIED"
  source_urls: []
  local_path: null
  status: "selected|alternative|excluded|pending"
  decision_reason: ""
  failure_notes: []
```

## 使用规则

- `identity_confidence` 反映导师作者归属是否可靠，不等于论文质量。
- `representativeness` 反映论文在导师研究主线中的位置，不以全文是否容易下载决定。
- `PDF_FULLTEXT_READ` 只在本地 PDF 已下载并实际读取后使用。
- `FULLTEXT_NON_PDF` 可以记录可靠 HTML/XML 全文，但不写成 PDF 精读。
- `ABSTRACT_ONLY` 和 `METADATA_ONLY` 不支持具体实验、方法机制或局限的正文表述。
- `IDENTITY_UNVERIFIED` 的成果不能进入导师代表作的确定性结论。
- 候选池不超过 3 篇时，先补充检索并记录回查范围；补充检索后仍然较少，报告可能是成果较少或公开资料不完整。
