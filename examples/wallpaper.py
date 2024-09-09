#!/bin/python3

import random
import os
import sys

wallpaper_path = "$Home/dokumente-sync/wallpaper"
wallpaper_old = "wallpaper_old.txt"
pre_args: str = "-x .csv --input $HOME/python/anime-dlp-2/tags.csv"


def main(args_str: str):

    get_img: str = os.popen(f"cft {args_str}").read()

    img_list: list = get_img.splitlines()

    # if str(img_list[1]).startswith("["):
    #     img_list_buffer: list = []
    #     for i in img_list:
    #         i = i[i.find("] ") + 2:i.find(" (")]
    #         img_list_buffer.append(i)

    #     img_list = []
    #     img_list = img_list_buffer

    try:
        with open(wallpaper_old, "r", encoding="utf-8") as file:
            wallpaper_old_img: str = file.readline()

    except FileNotFoundError:
        os.system(f"touch {wallpaper_old}")

    number: int = len(img_list) - 1
    pick_img: int = random.randint(0, number)

    if img_list[pick_img] == wallpaper_old_img:
        pick_img += 1

    if pick_img > number:
        pick_img = 0

    print(f"{wallpaper_path}/{img_list[pick_img]}")
    os.system(f'swww img "{wallpaper_path}/{img_list[pick_img]}"')

    with open(wallpaper_old, "w", encoding="utf-8") as file:
        file.writelines(img_list[pick_img])


def tofi() -> str:
    comand: str = os.popen('echo -e "any\nand\nnot\nrandom\ncostum" | tofi'
                           ).read().removesuffix("\n")
    if comand == "random":
        return "--list-files -d no"
    elif comand != "costum":
        tag: str = os.popen(f"echo $(cft {pre_args} --list-tags |"
                            f"tofi --prompt-text '{comand} ')"
                            ).read().removesuffix("\n")
        tag = tag[tag.find("] ") + 2:tag.find(" (")]
        return f'--{comand} "{tag}"'
    else:
        return os.popen("tofi --require-match=false").read().removesuffix("\n")


def args_func(args: list) -> str:
    args_str: str = ""
    for i in args:
        args_str += i
        args_str += " "
    return args_str


if __name__ == "__main__":
    args: list = (sys.argv[1:])
    if args == []:
        args_str: str = tofi()
    else:
        args_str: str = args_func(args)

    args_str = args_str.strip()
    args_str += f" {pre_args}"

    main(args_str)
