# это не шебанг!/usr/bin/env python

"""
Модуль brain_games.py Пока только приветсвие и запрос имени.

main() - пока только эта функция.
"""

from brain_games.cli import welcome_user


def main():
    """Главная функция."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
