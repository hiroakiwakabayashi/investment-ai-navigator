from database.client import supabase
from models.news import News


def save_news(news_list: list[News]):

    data = []

    for news in news_list:
        data.append({
            "id": news.id,
            "title": news.title,
            "url": news.url,
            "source": news.source,
            "published_at": news.published_at,
            "content": news.content,
        })

    return (
        supabase
        .table("news_raw")
        .upsert(
            data,
            on_conflict="id"
        )
        .execute()
    )
def get_waiting_news():

    result = (
        supabase
        .table("news_raw")
        .select("*")
        .eq("analysis_status", "waiting")
        .execute()
    )

    return result.data
def complete_analysis(news_id):

    return (
        supabase
        .table("news_raw")
        .update({
            "analysis_status": "completed"
        })
        .eq("id", news_id)
        .execute()
    )