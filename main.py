import requests, re, datetime, time

DISCORD_WEBHOOK_REGEX = re.compile(
    r"(https?:\/\/(ptb\.|canary\.)?discord(app)?\.com\/api\/webhooks\/(\d{18})\/([\w\-]{68}))"
)

with open("gists.txt") as f:
    PASTEBINS = f.read().splitlines()


def delete_webhook(webhook: str) -> None:
    with open("404.txt", "r+") as f:
        if webhook in f.read().splitlines():
            return
        f.write(webhook + "\n")
    print(requests.delete(webhook))

while True:
    for pastebin in PASTEBINS:
        resp = requests.get(pastebin, headers={"User-Agent": "AntiMalwareBot/gistscript (+https://discord.gg/TWhrmZFXqb)"})
        if resp.status_code != 200:
            print("Error: " + str(resp.status_code))
            continue
        for webhook in DISCORD_WEBHOOK_REGEX.findall(resp.text):
            delete_webhook(webhook[0])
    time.sleep(5)
