# Architecture

## システム構成

News Sources
    ↓
Collector
    ↓
Supabase
    ↓
AI Analyzer
    ↓
Publisher
    ↓
Website

---

## ディレクトリ構成

backend/
├── collector/
├── database/
├── ai/
├── publisher/
├── scheduler/
└── models/

---

## 開発方針

- collectorはニュース取得のみ
- databaseはDB操作のみ
- aiはAI分析のみ
- publisherは配信のみ
- schedulerは定期実行のみ