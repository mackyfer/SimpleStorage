from brownie import accounts, config, Storage, network


def deploy_storage():
    account = accounts[0]
    # account = accounts.add(config["wallets"]["from_key"])
    simple_storage = Storage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(10, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_storage()
