#Даны имена девочек. Определить, какие из этих имен встречаются в группах на всех вторых курсах,
#какие есть только в некоторых группах и какие не встречаются ни в одной из групп
girl_names = {'Альбина', 'Алина', 'София', 'Ирина', 'Настя', 'Вика', 'Елена', 'Марина', 'Мария'}
groups_on_second_year = [
    {"Альбина", "Мария", "Вика", "Ирина"},
    {"София", "Вика", "Альбина"},
    {"Вика", "Елена", "Настя", "Альбина"}
]

names_in_all_groups = set.intersection(*map(set, groups_on_second_year))

names_in_some_groups = set.union(*map(set, groups_on_second_year)) - names_in_all_groups

names_not_in_any_group = girl_names - set.union(*map(set, groups_on_second_year))

print("Имена девушек, встречающиеся во всех группах вторых курсов:", names_in_all_groups)
print("Имена девушек, которые есть в некоторых группах:", names_in_some_groups)
print("Имена девушек, которых нет ни в одной из групп:", names_not_in_any_group)
