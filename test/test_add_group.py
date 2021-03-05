from model.group import Group


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group().set_empty_parameters()
    app.group.create(group)

    # new list is longer, because we added 1 element
    assert app.group.count() == len(old_groups) + 1

    # if new list length is correct, then we can compare lists.
    # so we can get new list
    new_groups = app.group.get_group_list()

    # make sure that all elements of OLD list are in NEW list
    assert all(elem in new_groups for elem in old_groups)

    # built expected list for equalizing NEW and EXPECTED
    # expected = old _list + new_group. And sort()
    # sort() will use method __lt__, which was overridden
    old_groups.append(group)
    old_groups.sort()
    new_groups.sort()
    assert new_groups == old_groups


def test_add_handled_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name='any group', header='any header', footer='any footer')
    app.group.create(group)

    # new list is longer, because we added 1 element
    assert app.group.count() == len(old_groups) + 1

    # if new list length is correct, then we can compare lists.
    # so we can get new list
    new_groups = app.group.get_group_list()

    # make sure that all elements of OLD list are in NEW list
    assert all(elem in new_groups for elem in old_groups)

    # built expected list for equalizing NEW and EXPECTED
    # expected = old _list + new_group. And sort()
    # sort() will use method __lt__, which was overridden
    old_groups.append(group)
    old_groups.sort()
    new_groups.sort()
    assert new_groups == old_groups


def test_add_random_group(app):
    old_groups = app.group.get_group_list()
    group = Group().set_all_parameters_to_random_value()
    app.group.create(group)

    # new list is longer, because we added 1 element
    assert app.group.count() == len(old_groups) + 1

    # if new list length is correct, then we can compare lists.
    # so we can get new list
    new_groups = app.group.get_group_list()

    # make sure that all elements of OLD list are in NEW list
    assert all(elem in new_groups for elem in old_groups)

    # built expected list for equalizing NEW and EXPECTED
    # expected = old _list + new_group. And sort()
    # sort() will use method __lt__, which was overridden
    old_groups.append(group)
    old_groups.sort()
    new_groups.sort()
    assert new_groups == old_groups
