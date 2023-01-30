import pandas as pd
df =  pd.read_csv("INvideos.csv")
result = df

# result = df.head(10) :)

# result = df[5:15].head() :)

# result = df.columns :)
# result = len(df.columns) :)

df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","publish_time","trending_date"],axis=1,inplace=True) # :)
result = df
# result = df[["likes","dislikes"]].mean() :)

# result = df[["likes","dislikes"]].iloc[:50] # :)
# result = df.head(50)[["likes","dislikes","channel_title"]] # Hocanın Yaptığı.

# result = df[df["views"] == df["views"].max()]["title"].iloc[0] :)
# result = df[df["views"] == df["views"].max()][["title","views"]] # Hocanın ilk yaptığı / normal şekilde ki benim yaptığımın aynısı (26.rows)


# result = df[df["views"] == df["views"].min()]["channel_title"].iloc[0] :)


# result = df.nlargest(10,"views")[["title","views"]] # benim yaptığım => .nlargest metoduyla.
# result = df.sort_values("views",ascending=False).head(10)[["views","title"]] # hocanın yaptığı


# result = df.groupby("category_id").mean()["likes"].sort_values() # ::)
# result = df.groupby("category_id").mean().sort_values("likes")["likes"] # ek olarak yaptığım ve hocanın yaptığı <=


# result = df.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"]

# 
# result = df["category_id"].value_counts()
    

# df["title_len"] = df["title"].apply(len)


# df["tag_number"] = df["tags"].apply(lambda x: len(x.split("|")))
def tagcount(tag):
    return len(tag.split("|"))
df["tag_number"] = df["tags"].apply(tagcount)


# likesList = list(df["likes"].head())
# dislikesList = list(df["dislikes"].head())
# print(likesList,dislikesList)

def oranhesapla(datasets):
    likesList = list(datasets["likes"])
    dislikeList = list(datasets["dislikes"])
    
    liste = list(zip(likesList,dislikeList)) 
    oranList = []
    for like,dislike in liste:
        if (like+dislike) == 0:
            oranList.append(0)
        else:
            oranList.append(like/(like+dislike))

    
    
    return oranList


df["begeni_oranı"] = oranhesapla(df) 
print(df.sort_values("begeni_oranı",ascending=False)[["title","likes","dislikes","begeni_oranı"]])