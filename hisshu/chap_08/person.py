# Chapter.08 関数
# ## 戻り値
# ### 辞書を返す
print("\n### 辞書を返す\n")

def build_person(first_name, last_name, age=None):
    """人についての情報を辞書で返す"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
