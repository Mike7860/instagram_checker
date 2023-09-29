from html.parser import HTMLParser
from bs4 import BeautifulSoup

# To one time using
# with open("followers_02_02_2023.html", "r", encoding='utf-8') as f:
#     followers_links = []
#     soup = BeautifulSoup(f, "html.parser")
#     href_tags = soup.find_all(href=True)
#     for href in href_tags:
#         followers_links.append(href.get('href'))
#     #print(followers_links)


def save_to_txt(data):
    with open("02_02_2023_followers.txt", "w", encoding='utf-8') as txt_file:
        for link in data:
            txt_file.write(link + '\n')
        print(txt_file)

#save_to_txt(followers_links)


def find_bots():
    followers_links = []
    with open("02_02_2023_followers.txt", "r", encoding='utf-8') as txt:
        for t in txt:
            followers_links.append(t.rstrip('\n'))

    with open("followers_1.html", "r", encoding='utf-8') as f:
        current_followers_links = []
        new_followers_links_to_add = []
        bots = []
        soup = BeautifulSoup(f, "html.parser")
        href_tags = soup.find_all(href=True)
        for href in href_tags:
            current_followers_links.append(href.get('href'))
            if href.get('href') not in followers_links:
                new_followers_links_to_add.append(href.get('href'))
        for old in followers_links:
            if old not in current_followers_links:
                bots.append(old)
                followers_links.remove(old)
                print(old)
    with open("02_02_2023_followers.txt", "w", encoding='utf-8') as f:
        for actual in followers_links:
            f.write(actual + '\n')
    with open("02_02_2023_followers.txt", "a", encoding='utf-8') as f:
        for new_to_add in new_followers_links_to_add:
            f.write(new_to_add + '\n')
    with open("bots.txt", "w", encoding='utf-8') as b:
        for bot in bots:
            b.write(bot + '\n')
    print(len(followers_links))
    #print(followers_links)
    return "Bots or changed nicks: {}".format(bots)


print(find_bots())



def followed_but_not_following():
    followers_links = []
    with open("02_02_2023_followers.txt", "r", encoding='utf-8') as txt:
        for t in txt:
            followers_links.append(t.rstrip('\n'))
    with open("following.html", "r", encoding='utf-8') as f:
        current_following_links = []
        new_following_to_check = []
        soup = BeautifulSoup(f, "html.parser")
        href_tags = soup.find_all(href=True)
        for href in href_tags:
            current_following_links.append(href.get('href'))
            if href.get('href') not in followers_links:
                new_following_to_check.append(href.get('href'))



        # for old in followers_links:
        #     if old not in current_following_links:
        #         # Todo pop method with deleting bots
        #         #bots.append(old)
    return "Followers WIDMO or nick changed: {}".format(new_following_to_check)























#Todo maybe profiling??
















print(followed_but_not_following())


