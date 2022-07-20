import math
max = 4
ar = [1,2,3,4,5,6,7]
a = len(ar)
print(math.ceil(a/4))

ar1 = []
ar2 = [] 
ar3 = []

for num in ar:
    if len(ar1) == len(ar2) == len(ar3):
        ar1.append(num)
    elif len(ar2) == len(ar3):
        ar2.append(num)
    else:
        ar3.append(num)
        
print(ar1)
print(ar2)
print(ar3)


# draft :
_list = User.objects.values_list('id',flat=True).order_by('-created_on')[:100]

User.objects.filter(id__in=list(u_list)).delete()


>>> ul = User.objects.all().last()
>>> ul
<User: Brown.Gulgowski>
>>> ul.delete()
(6, {'accounts.ProfilePicture': 1, 'accounts.Settings': 1, 'topliker.UserPoint': 1, 'socialapp.Friend': 1, 'fcm_django.FCMDevice': 1, 'accounts.User': 1})
>>> uf = User.objects.all().first()
>>> uf
<User: Karlee_Gislason>
>>> uf = User.objects.filter().order_by('created_on').first()
>>> uf
<User: admin>
>>> uf = User.objects.filter().order_by('-created_on').first()
>>> uf
<User: Gerald11>
>>> uf = User.objects.filter().order_by('-created_on')[:1]
>>> uf
<QuerySet [<User: Gerald11>]>
>>> uf = User.objects.filter().order_by('created_on')[:1]
>>> uf
<QuerySet [<User: admin>]>
>>> uf = User.objects.filter().order_by('-created_on')[:100]
>>> uf
<QuerySet [<User: Gerald11>, <User: Stewart52>, <User: Marta93>, <User: Ceasar_Watsica>, <User: Hayley.Doyle>, <User: Candace.Bartoletti>, <User: Wilfred.Conroy>, <User: Elsie61>, <User: Gene_Wisozk>, <User: Novella.Rempel49>, <User: Thad_Wolff>, <User: Abelardo_Douglas>, <User: Tommie_Yundt59>, <User: Dimitri_Torphy74>, <User: Norma_Brekke68>, <User: Claudie38>, <User: Ariane.Miller>, <User: Dayana.Bailey20>, <User: Estrella.Bins96>, <User: Obie_Murray74>, '...(remaining elements truncated)...']>
>>> uf.filter(username='admin')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/query.py", line 941, in filter
    return self._filter_or_exclude(False, args, kwargs)
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/query.py", line 953, in _filter_or_exclude
    assert not self.query.is_sliced, \
AssertionError: Cannot filter a query once a slice has been taken.
>>> uf
<QuerySet [<User: Gerald11>, <User: Stewart52>, <User: Marta93>, <User: Ceasar_Watsica>, <User: Hayley.Doyle>, <User: Candace.Bartoletti>, <User: Wilfred.Conroy>, <User: Elsie61>, <User: Gene_Wisozk>, <User: Novella.Rempel49>, <User: Thad_Wolff>, <User: Abelardo_Douglas>, <User: Tommie_Yundt59>, <User: Dimitri_Torphy74>, <User: Norma_Brekke68>, <User: Claudie38>, <User: Ariane.Miller>, <User: Dayana.Bailey20>, <User: Estrella.Bins96>, <User: Obie_Murray74>, '...(remaining elements truncated)...']>
>>> uf.delete()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/query.py", line 724, in delete
    assert not self.query.is_sliced, \
AssertionError: Cannot use 'limit' or 'offset' with delete.
>>> User.objects.filter(id__in=list(uf).delete()
... 
... 
... )
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'list' object has no attribute 'delete'
>>> User.objects.filter(id__in=list(uf)).delete()
Traceback (most recent call last):
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/fields/__init__.py", line 2434, in to_python
    return uuid.UUID(**{input_form: value})
  File "/usr/lib/python3.8/uuid.py", line 168, in __init__
    hex = hex.replace('urn:', '').replace('uuid:', '')
AttributeError: 'User' object has no attribute 'replace'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/query.py", line 941, in filter
    return self._filter_or_exclude(False, args, kwargs)
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/query.py", line 961, in _filter_or_exclude
    clone._filter_or_exclude_inplace(negate, args, kwargs)
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/query.py", line 968, in _filter_or_exclude_inplace
    self._query.add_q(Q(*args, **kwargs))
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/sql/query.py", line 1393, in add_q
    clause, _ = self._add_q(q_object, self.used_aliases)
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/sql/query.py", line 1412, in _add_q
    child_clause, needed_inner = self.build_filter(
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/sql/query.py", line 1347, in build_filter
    condition = self.build_lookup(lookups, col, value)
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/sql/query.py", line 1193, in build_lookup
    lookup = lookup_class(lhs, rhs)
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/lookups.py", line 25, in __init__
    self.rhs = self.get_prep_lookup()
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/lookups.py", line 240, in get_prep_lookup
    rhs_value = self.lhs.output_field.get_prep_value(rhs_value)
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/fields/__init__.py", line 2418, in get_prep_value
    return self.to_python(value)
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/fields/__init__.py", line 2436, in to_python
    raise exceptions.ValidationError(
django.core.exceptions.ValidationError: ['“Gerald11” is not a valid UUID.']
>>> u_list = User.objects.values_list('id',flat=true).order_by('-created_on')[:100]
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'true' is not defined
>>> u_list = User.objects.values_list('id',flat=True).order_by('-created_on')[:100]
>>> u_list
<QuerySet [UUID('ee74fe0b-dcd4-4e1a-aee1-0a7297f2bbd9'), UUID('5eea3a92-c93d-4777-a1ef-5aa19f7710c2'), UUID('bd8781f2-87c5-4a5d-8798-b376971712a7'), UUID('1c1c4883-8a2f-4377-bc00-3cce102ddb2d'), UUID('c3aaa38b-ab02-4b74-b8d8-c158ae07b362'), UUID('d895fb7b-9493-42bd-967d-c686318dc695'), UUID('c00bef44-56d7-43de-8d92-e74d30c496f0'), UUID('10b5c4ad-1dfd-45b6-80f9-0445bd88596a'), UUID('b9bf3f8d-18c8-446d-9f94-b3977ea3a478'), UUID('76de75d4-a3c3-44ec-8477-30923840b8f3'), UUID('89aca9a2-dd4b-4636-92cc-31a2af8fa415'), UUID('08f49995-0a98-4556-9a97-872b8b922117'), UUID('1edb5ae4-cddd-4fcb-b72a-e49d8f087df9'), UUID('16f495d5-3e0a-4f5f-b69d-962748bf4ebf'), UUID('ac3824a3-9e7c-4e53-a251-b3f752087c11'), UUID('4a834e09-5150-4628-a6a8-e5194b99c09e'), UUID('865bd1f4-6bdc-479f-83a7-12ed7f8232cf'), UUID('bd3e2b03-b461-43ba-8f80-b1d7b65e89a8'), UUID('2eecc6e5-2a78-4d29-a725-08b02cfe8171'), UUID('b2e9ec5c-86a1-4bed-b9b4-2b9fa5f12fdf'), '...(remaining elements truncated)...']>
>>> User.objects.filter(id__in=list(u_list)).delete()
(700, {'accounts.ProfilePicture': 100, 'accounts.Settings': 100, 'topliker.UserPoint': 100, 'topliker.UserGroup': 100, 'socialapp.Friend': 100, 'fcm_django.FCMDevice': 100, 'accounts.User': 100})
>>> ul
<User: Brown.Gulgowski>
>>> u_list = User.objects.values_list('id',flat=true).order_by('-created_on')[:100]
KeyboardInterrupt
>>> u_list = User.objects.values_list('id',flat=True).order_by('-created_on')[:100]
>>> User.objects.filter(id__in=list(u_list)).delete()
(972, {'accounts.ProfilePicture': 97, 'accounts.Settings': 97, 'topliker.UserPoint': 97, 'topliker.UserGroup': 384, 'socialapp.Friend': 97, 'fcm_django.FCMDevice': 100, 'accounts.User': 100})
>>> u_list
<QuerySet [UUID('f2fc39cb-5c36-4be3-9145-91dc26bc9cec'), UUID('e674db74-523d-4316-bb6d-182bd4c056d1'), UUID('a15264b9-38ab-4bf0-bfb5-067833b96cb3'), UUID('88adfcbc-8c8e-4aa2-b9cc-cb1f59f10cb4'), UUID('b1bf9ce5-ff3d-46ae-bb44-45412e34be26'), UUID('dbd03be8-403a-4bfb-b05c-7725a6e08bbf'), UUID('4891882e-15cf-4084-9103-64a09988223e'), UUID('98657b4c-01c7-441f-b3bb-f5364660cb89'), UUID('bfad5983-e7cd-4a48-b096-ea03b7f0c8a7'), UUID('2b48bc1f-c177-4d23-b61d-80d46f8c2f54'), UUID('34e1b05b-9c42-47c5-8c89-3ac600a82d99'), UUID('3f426124-1d04-4fb6-b595-47d1ab5ced6e'), UUID('e9c50925-438e-46af-a994-ef083b1ee38e'), UUID('bd98696c-e497-4cb0-b6b4-55c76e73fe31'), UUID('e2b23551-6b7e-42c3-b0e7-06f8b960edea'), UUID('0df2f1e2-d71d-42d4-ad3c-0dca4ddfbb7f'), UUID('c01d6760-6fbd-4508-924f-47921276664c'), UUID('7cbd5b20-ac9d-452e-bf8b-0df21560e1b0'), UUID('11fadd59-2e35-495f-bc19-d096dbb177a5'), UUID('5596c08c-32a1-467e-ae06-fbb241304ab5'), '...(remaining elements truncated)...']>
>>> User.objects.filter(id__in=list(u_list)).delete()
(0, {})
>>> u_list
<QuerySet [UUID('f2fc39cb-5c36-4be3-9145-91dc26bc9cec'), UUID('e674db74-523d-4316-bb6d-182bd4c056d1'), UUID('a15264b9-38ab-4bf0-bfb5-067833b96cb3'), UUID('88adfcbc-8c8e-4aa2-b9cc-cb1f59f10cb4'), UUID('b1bf9ce5-ff3d-46ae-bb44-45412e34be26'), UUID('dbd03be8-403a-4bfb-b05c-7725a6e08bbf'), UUID('4891882e-15cf-4084-9103-64a09988223e'), UUID('98657b4c-01c7-441f-b3bb-f5364660cb89'), UUID('bfad5983-e7cd-4a48-b096-ea03b7f0c8a7'), UUID('2b48bc1f-c177-4d23-b61d-80d46f8c2f54'), UUID('34e1b05b-9c42-47c5-8c89-3ac600a82d99'), UUID('3f426124-1d04-4fb6-b595-47d1ab5ced6e'), UUID('e9c50925-438e-46af-a994-ef083b1ee38e'), UUID('bd98696c-e497-4cb0-b6b4-55c76e73fe31'), UUID('e2b23551-6b7e-42c3-b0e7-06f8b960edea'), UUID('0df2f1e2-d71d-42d4-ad3c-0dca4ddfbb7f'), UUID('c01d6760-6fbd-4508-924f-47921276664c'), UUID('7cbd5b20-ac9d-452e-bf8b-0df21560e1b0'), UUID('11fadd59-2e35-495f-bc19-d096dbb177a5'), UUID('5596c08c-32a1-467e-ae06-fbb241304ab5'), '...(remaining elements truncated)...']>
>>> u_list = User.objects.values_list('id',flat=True).order_by('-created_on')[:80]
>>> User.objects.filter(id__in=list(u_list)).delete()
(560, {'accounts.ProfilePicture': 80, 'accounts.Settings': 80, 'topliker.UserPoint': 80, 'topliker.UserGroup': 80, 'socialapp.Friend': 80, 'fcm_django.FCMDevice': 80, 'accounts.User': 80})
>>> ug2 = user_group in UserGroup.objects.filter().order_by('points')
>>> ug2
False
>>> ug2 = UserGroup.objects.filter().order_by('points')
>>> ug2
<QuerySet [<UserGroup: Maggie_Collier62>, <UserGroup: Daniela_Altenwerth>, <UserGroup: Donna.Lakin>, <UserGroup: Gayle6>, <UserGroup: Ocie.Rosenbaum>, <UserGroup: Gilberto_Pouros>, <UserGroup: Mellie_Huels>, <UserGroup: Blaze23>, <UserGroup: Marge.Reichel64>, <UserGroup: Kathryn_Brown>, <UserGroup: Hubert_Cronin41>, <UserGroup: Vince33>, <UserGroup: Xander26>, <UserGroup: Ava_Rolfson36>, <UserGroup: Joelle_Ruecker84>, <UserGroup: Kiel66>, <UserGroup: Melissa.Parisian>, <UserGroup: Rosie50>, <UserGroup: Emerson.Spencer>, <UserGroup: Mckenzie_Reichel>, '...(remaining elements truncated)...']>
>>> ug2.first().points
0.0
>>> ug2 = Group.objects.filter().order_by('toatal_users_count')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/query.py", line 1149, in order_by
    obj.query.add_ordering(*field_names)
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/sql/query.py", line 1993, in add_ordering
    self.names_to_path(item.split(LOOKUP_SEP), self.model._meta)
  File "/home/jadon6/Documents/WhatsLike-BackEnd/env/lib/python3.8/site-packages/django/db/models/sql/query.py", line 1539, in names_to_path
    raise FieldError("Cannot resolve keyword '%s' into field. "
django.core.exceptions.FieldError: Cannot resolve keyword 'toatal_users_count' into field. Choices are: created_at, group, id, is_active, total_users_count
>>> ug2 = Group.objects.filter().order_by('total_users_count')
>>> ug2
<QuerySet [<Group: 2022-07-20>, <Group: 2022-07-20>, <Group: 2022-07-20>, <Group: 2022-07-20>, <Group: 2022-07-20>, <Group: 2022-07-20>, <Group: 2022-07-20>, <Group: 2022-07-20>]>
>>> ug2.fisrt().total_users_count
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'fisrt'
>>> ug2.first().total_users_count
89
>>> ug2.last().total_users_count
90
>>> Group.objects.filter().order_by('total_users_count').first()
<Group: 2022-07-20>
>>> Group.objects.filter().order_by('total_users_count').first()
>>> aaa = Group.objects.filter().order_by('total_users_count').first()
>>> aaa
>>> aaa
>>> Group.objects.filter().order_by('total_users_count')
<QuerySet []>
>>> aaa
>>> aaa = Group.objects.filter().order_by('total_users_count').first()
>>> aaa
<Group: 2022-07-20>
>>> aaa = Group.objects.filter().order_by('total_users_count').first()
>>> aaa
<Group: 2022-07-20>
>>> aaa = Group.objects.filter().order_by('total_users_count').first().total_usesrs_count
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Group' object has no attribute 'total_usesrs_count'
>>> aaa = Group.objects.filter().order_by('total_users_count').first().total_users_count
>>> aaa
89
>>> aaa = Group.objects.filter().order_by('total_users_count').first()
>>> aaa
<Group: 2022-07-20>
>>> aaa.id
UUID('7be6dac0-4155-492c-9650-32f7539b5505')
>>> aaa = Group.objects.filter().order_by('total_users_count').first()
>>> aaa.id
UUID('a1f98eb8-7db2-40ea-9d8a-8af85dd95f26')
>>> aaa = Group.objects.filter().order_by('total_users_count').first()
>>> aaa.id
UUID('a1f98eb8-7db2-40ea-9d8a-8af85dd95f26')
>>> aaa = Group.objects.filter().order_by('total_users_count').first()
>>> aaa.id
UUID('d2e2953c-8f4e-4403-8380-267563888be3')