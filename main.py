import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)
        for player in players:
            current_race, _ = Race.objects.get_or_create(name=player[
                "race"
            ]["name"], defaults={"description": player[
                "race"
            ].get("description", "")})

            for skill in player.get("skills", []):
                Skill.objects.get_or_create(name=skill[
                    "name"
                ], defaults={"bonus": skill.get("bonus",
                                                ""), "race": current_race})

            if player.get("guild") is None:
                current_guild = None
            else:
                current_guild, _ = Guild.objects.get_or_create(name=player[
                    "guild"
                ]["name"], defaults={"description": player[
                    "guild"
                ].get("description", "")})
            Player.objects.get_or_create(nickname=player.get("nickname"),
                                         email=player.get("email"),
                                         bio=player.get("bio"),
                                         race=current_race,
                                         guild=current_guild)


if __name__ == "__main__":
    main()
