from database.client import supabase


def save_analysis(result):

    return (
        supabase
        .table("news_analysis")
        .insert(result)
        .execute()
    )

def get_completed_analysis():

    response = (

        supabase
        .table("news_analysis")
        .select("*")
        .execute()

    )

    return response.data