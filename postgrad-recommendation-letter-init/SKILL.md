---
name: postgrad-recommendation-letter-init
description: "初始化或更新保研自荐信工作流的个人简历资料与可选自荐信底稿。"
metadata:
  short-description: "初始化简历与自荐信底稿"
---

# 保研自荐信初始化

这是入口 skill，只负责建立和维护使用者的简历资料与自荐信底稿上下文。它不调研导师、不下载或精读论文、不改写某位导师的信。完成初始化后，使用 `$postgrad-recommendation-letter-run` 执行具体导师任务。

## 首次调用

如果当前工作区没有可用的 `.postgrad-recommendation-letter/profile.json`，主动索取：

> 请上传个人简历（必需，PDF/DOCX 均可）。如果有希望沿用版式和写作风格的自荐信模板，也可以一并上传，但模板是可选的；不上传时使用通用默认模板。

简历是初始化的必需材料。读取简历后整理姓名、教育、成绩、推免资格、科研、竞赛、奖项、技能和申请偏好；每项事实保留来源，示例值、星号和疑似模板占位符标为待确认，不能直接进入正式信件。

用户上传模板时，将完整 DOCX 登记为后续实际改写底稿，保留其版式、段落组织和语气偏好。模板中的姓名、学校、成绩、旧导师、旧论文和旧研究方向不自动当作用户事实。用户不上传模板时，登记内置默认 DOCX。

## 已初始化时

读取状态并简要展示当前简历和底稿状态，询问用户是继续使用、更新简历、还是更换底稿。用户提供“满意稿”“以后沿用”等明确指令和 DOCX 时，将该文件登记为新的底稿；不要把其中的导师事实写入个人资料。

## 状态接口

状态文件固定为当前工作区的 `.postgrad-recommendation-letter/profile.json`，结构见 [profile-schema.md](references/profile-schema.md)。入口写入，执行 skill 只读。

初始化完成后告知用户：

> 初始化完成。现在使用 `$postgrad-recommendation-letter-run`，指定学校、学院、导师和可选主页链接，即可开始完整调研、论文精读、自荐信改写与 DOCX 交付。

示例：

`使用 $postgrad-recommendation-letter-run，调研【学校】【学院】的【导师】老师；官网主页：【可选 URL】。完成完整流程并输出 DOCX。`

## 读取默认模板

无用户模板时使用 `assets/default-letter-template.docx`，通用段落结构见 [default-template.md](references/default-template.md)。
