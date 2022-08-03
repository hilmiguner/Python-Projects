from time import process_time
import pandas as pd

df = pd.read_csv(filepath_or_buffer="Module Pandas/datasets/England-Youtube.csv")

# 1- İlk 10 kaydı getiriniz.
print(f"1- İlk 10 kaydı getiriniz: \n{df.head(10)}")

print(100*"*")

# 2- İkinci 5 kaydı getiriniz.
result = df.loc[5:, :].head()
print(f"2- İkinci 5 kaydı getiriniz: \n{result}")

print(100*"*")

# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
columns = df.columns
print(f"3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz: \n{columns}, {len(columns)}")

print(100*"*")

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
result = df.drop(["thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"], axis=1)
print(f"4- Kolonu silinmiş dataframe: \n{result.head()}")

print(100*"*")

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
result = [df["likes"].mean(), df["dislikes"].mean()]
print(f"5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz. Like -> {result[0]}, Dislike -> {result[1]}")

print(100*"*")

# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
result = df[["likes", "dislikes"]].head(50)
print(f"6- ilk 50 videonun like ve dislike kolonlarını getiriniz: \n{result}")

print(100*"*")

# 7- En çok görüntülenen video hangisidir ?
result = df[df["views"] == df["views"].max()][["title", "views"]]
print(f"7- En çok görüntülenen video hangisidir: \n{result}")

print(100*"*")

# 8- En düşük görüntülenen video hangisidir?
result = df[df["views"] == df["views"].min()][["title", "views"]]
print(f"8- En düşük görüntülenen video hangisidir: \n{result}")

print(100*"*")

# 9- En fazla görüntülenen ilk 10 video hangisidir ?
result = df.sort_values("views", ascending=False).head(10)[["title", "views"]]
print(f"9- En fazla görüntülenen ilk 10 video hangisidir: \n{result}")

print(100*"*")

# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
result = df.groupby("category_id").mean().sort_values("likes")["likes"]
print(f"10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz: \n{result}")

print(100*"*")

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
result = df.groupby("category_id").sum().sort_values("comment_count", ascending=False)["comment_count"]
print(f"11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız: \n{result}")

print(100*"*")

# 12- Her kategoride kaç video vardır ?
result = df["category_id"].value_counts()
print(f"12- Her kategoride kaç video vardır: \n{result}")

print(100*"*")

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df["len_of_title"] = df["title"].apply(len)
temp = df[["title", "len_of_title"]]
print(f"13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz: \n{temp}")

print(100*"*")

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
def find_len(x):
    if x == "[none]":
        return 0
    return len(x.split("|"))

df["tags_count"] = df["tags"].apply(find_len)
result = df[["tags", "tags_count"]].head()
print(f"14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz: \n{result}")
    
print(100*"*")

# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)
def ratio(dataframe: pd.DataFrame):
    ratio = []
    like_list = []
    dislike_list = []
    for i in dataframe["likes"]:
        like_list.append(int(i))
    for i in dataframe["dislikes"]:
        dislike_list.append(int(i))
    for i in range(0, len(like_list)):
        try:
            ratio.append(like_list[i]/dislike_list[i])
        except ZeroDivisionError as err:
            ratio.append(like_list[i])
    dataframe["ratio"] = pd.Series(data=ratio)
    result = dataframe.sort_values("ratio", ascending=False)[["title", "likes", "dislikes", "ratio"]].head(100)
    return result

print(f"15- En popüler videoları listeleyiniz.(like/dislike oranına göre): \n{ratio(df)}")