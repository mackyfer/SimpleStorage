from brownie import Storage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    storage = Storage.deploy({"from": account})
    starting_value = storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_storing():
    # Arrange
    account = accounts[0]
    storage = Storage.deploy({"from": account})
    expected = 15
    # Act
    storage.store(expected, {"from": account})

    # Assert
    assert storage.retrieve() == expected
