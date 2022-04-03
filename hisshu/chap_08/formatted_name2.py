# Chapter.08 関数
# ## 戻り値
# ### オプション引数を作成する
print("\n### オプション引数を作成する\n")

def get_formatted_name(first_name,  last_name, middle_name=''):
    """フォーマットされたフルネームを返す"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
