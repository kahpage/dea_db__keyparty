# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    disabled_events: list[int | str] = []

    i = 1  # ==== keyparty1 ====
    if i not in disabled_events:
        event_name = f"keyparty{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "01_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20261025180224/https://mattari-an.net/keyparty/1st/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="チラシ絵提供：猫足とろろ 様（とろろのお宿）",
            ),
            Medium(
                "01_20101230125836_bnrkp.png",
                [
                    Source(
                        "https://web.archive.org/web/20101230125836/http://mattari-an.net/keyparty/bnrkp.png",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            Medium(
                "01_titlelogo.gif",
                [
                    Source(
                        "https://web.archive.org/web/20261025180224/https://mattari-an.net/keyparty/1st/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "01_kannai.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20261025180229/https://mattari-an.net/keyparty/1st/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "01_kannai.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20261025180229/https://mattari-an.net/keyparty/1st/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.01365, 135.7809429),
                address="9-1 Okazaki Seishojicho, Sakyo Ward, Kyoto, 606-8343, Japan",
                description="京都市勧業館　みやこめっせ　３階 第３展示場Ａ面 第３展示場全面",
                sources=[
                    Source(
                        "https://web.archive.org/web/20261025180224/https://mattari-an.net/keyparty/1st/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlur6oWztq77DaOuTZLw5MRyj3iDVD1CD-wl9_7wkEXC7e9JYhls5YX8XY6_936CE_RWP6CozLolZI73Mh7gleO-PgU9DJro4VpNaq7nQSPaHd9rChZ-VVge7urD47mbsVOMZ6B-A=s870-k-no",
                url="https://maps.app.goo.gl/8MjxYFEFKBxjhyTT8",
            ),
        ]
        event = Event(
            aliases=["Keyパーティー", "Key Party", "Keyパーティー1", "Key Party 1"],
            dates="2011.03.27",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20261025180224/https://mattari-an.net/keyparty/1st/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20261025180229/https://mattari-an.net/keyparty/1st/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2025.10.25",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== keyparty2 ====
    if i not in disabled_events:
        event_name = f"keyparty{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "02_20110721214853_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20110721214853/http://mattari-an.net/keyparty/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="チラシ絵提供：猫足とろろ 様（とろろのお宿）",
            ),
            Medium(
                "02_20110721214853_titlelogo.gif",
                [
                    Source(
                        "https://web.archive.org/web/20110721214853/http://mattari-an.net/keyparty/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            Medium(
                "02_bnrkp.png",
                [
                    Source(
                        "https://web.archive.org/web/20110917022631/http://mattari-an.net/littlebusters/index.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1708859, 136.8837218),
                address="4-chōme-4-38 Meieki, Nakamura Ward, Nagoya, Aichi 450-0002, Japan",
                description="愛知県産業労働センター（ウインクあいち）　６階展示場",
                sources=[
                    Source(
                        "https://web.archive.org/web/20110721214853/http://mattari-an.net/keyparty/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://streetviewpixels-pa.googleapis.com/v1/thumbnail?output=thumbnail&cb_client=maps_sv.tactile.gps&panoid=plEI7dd2WTUE58egOJKX3g&w=1177&h=1300&yaw=170&pitch=-40",
                url="https://maps.app.goo.gl/6F2N7Dtys66bRMQQ9",
            ),
        ]
        event = Event(
            aliases=["Keyパーティー2", "Key Party 2"],
            dates="2011.09.11",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20110721214853/http://mattari-an.net/keyparty/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20110918034246/http://mattari-an.net/angelbeats/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2025.10.25",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 3  # ==== keyparty3 ====
    if i not in disabled_events:
        event_name = f"keyparty{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "03_20120120221722_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20120120221722/http://mattari-an.net/keyparty/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="チラシ絵提供：猫足とろろ 様（とろろのお宿）",
            ),
            Medium(
                "03_20120120221722_titlelogo.gif",
                [
                    Source(
                        "https://web.archive.org/web/20120120221722/http://mattari-an.net/keyparty/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            Medium(
                "03_29939431_p0_master1200.jpg",
                [
                    Source(
                        "https://www.pixiv.net/en/artworks/29939431",
                        (RT.Reliable, OT.OfficialExt),
                    )
                ],
                comments="Official (raw) catalog artwork for the event, as stated in the pixiv page description.",
            ),
            Medium(
                "03_kannai.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20250324061852/https://mattari-an.net/angelbeats/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1590924, 136.9298891),
                address="2 Chome-6-3 Fukiage, Chikusa Ward, Nagoya, Aichi 464-0856, Japan",
                description="名古屋中小企業福祉会館　６階ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20120120221722/http://mattari-an.net/keyparty/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkq7ADwtY0_LzlU3mk0DFlmJeNo1bo9bpZ2vqyiopbdHLCB4zA_pSkSpa9YKGQsJgPRhkx6a0R8e8OPBlstCq-5saYTJ5-avtnX6fZR-cI6YHIZgV7pYeOLMsw_PDlSU2wW-9f9=s0?imgmax=0",
                url="https://maps.app.goo.gl/5QerDbUB3hz5Xcjq9",
            ),
        ]
        event = Event(
            aliases=["Keyパーティー3", "Key Party 3"],
            dates="2012.09.16",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20120120221722/http://mattari-an.net/keyparty/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20161227222754/http://mattari-an.net/angelbeats/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2025.10.25",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 4  # ==== keyparty4 ====
    if i not in disabled_events:
        event_name = f"keyparty{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "04_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20240416105205/http://mattari-an.net/littlebusters/index.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "04_33546618_p0.png",
                [
                    Source(
                        "https://www.pixiv.net/en/artworks/33546618",
                        (RT.Reliable, OT.OfficialExt),
                    )
                ],
                comments="Official (raw) catalog artwork for the event, as seen here: http://kpckg.blog.fc2.com/blog-entry-52.html",
            ),
            Medium(
                "04_20250413230521_bnrkp41.png",
                [
                    Source(
                        "https://web.archive.org/web/20250413230521/http://mattari-an.net/keyparty/bnrkp41.png",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "04_20250413230521_bnrkp42.png",
                [
                    Source(
                        "https://web.archive.org/web/20250413230521/http://mattari-an.net/keyparty/bnrkp42.png",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "04_20250413230521_bnrkp44.png",
                [
                    Source(
                        "https://web.archive.org/web/20250413230521/http://mattari-an.net/keyparty/bnrkp44.png",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "04_20250413230521_bnrkp45.png",
                [
                    Source(
                        "https://web.archive.org/web/20250413230521/http://mattari-an.net/keyparty/bnrkp45.png",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "04_kannai.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20130212182116/http://mattari-an.net/littlebusters/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "04_zenkan.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20260511000444/http://mattari-an.net/littlebusters/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.01365, 135.7809429),
                address="9-1 Okazaki Seishojicho, Sakyo Ward, Kyoto, 606-8343, Japan",
                description="京都市勧業館 みやこめっせ　３階 第３展示場",
                sources=[
                    Source(
                        "https://web.archive.org/web/20130218043158/http://mattari-an.net:80/keyparty/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlur6oWztq77DaOuTZLw5MRyj3iDVD1CD-wl9_7wkEXC7e9JYhls5YX8XY6_936CE_RWP6CozLolZI73Mh7gleO-PgU9DJro4VpNaq7nQSPaHd9rChZ-VVge7urD47mbsVOMZ6B-A=s870-k-no",
                url="https://maps.app.goo.gl/8MjxYFEFKBxjhyTT8",
            ),
        ]
        event = Event(
            aliases=["Keyパーティー4", "Key Party 4"],
            dates="2013.03.24",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20130218043158/http://mattari-an.net:80/keyparty/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20260511000444/http://mattari-an.net/littlebusters/list.html",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    'Participating circles of Key Party being "パ" positions (鍵 for リトバスパーティーR)',
                    (RT.Guess, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2025.10.25",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 5  # ==== keyparty5 ====
    if i not in disabled_events:
        event_name = f"keyparty{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "05_bnrkp.png",
                [
                    Source(
                        "https://web.archive.org/web/20130504130836/http://ttc.ninja-web.net/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1708859, 136.8837218),
                address="4-chōme-4-38 Meieki, Nakamura Ward, Nagoya, Aichi 450-0002, Japan",
                description="名古屋企業福祉会館　６階ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20130615162020/http://mattari-an.net/keyparty/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://streetviewpixels-pa.googleapis.com/v1/thumbnail?output=thumbnail&cb_client=maps_sv.tactile.gps&panoid=plEI7dd2WTUE58egOJKX3g&w=1177&h=1300&yaw=170&pitch=-40",
                url="https://maps.app.goo.gl/6F2N7Dtys66bRMQQ9",
            ),
        ]
        event = Event(
            aliases=["Keyパーティー5", "Key Party 5"],
            dates="2013.09.15",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20130615162020/http://mattari-an.net/keyparty/",
                    (RT.Reliable, OT.Official),
                ),
                # Source("Participating circles: ", (RT.Reliable, OT.Official)),
            ],
            locations=locations,
            description="Unlike similar events, no /5th/ pages were saved, so the participating circles are unknown for now.",
            # comments=None,
            last_edited="2025.10.25",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 6  # ==== keyparty6 ====
    if i not in disabled_events:
        event_name = f"keyparty{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "06_20140426153732_paper.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20260417110414/https://mattari-an.net/keyparty/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            Medium(
                "06_20140426153732_titlelogo.gif",
                [
                    Source(
                        "https://web.archive.org/web/20260417110414/https://mattari-an.net/keyparty/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            Medium(
                "06_kannai.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20260609183908/http://mattari-an.net/keyparty/list.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "06_20160429115231_bnrkp61.png",
                [
                    Source(
                        "https://web.archive.org/web/20160429115231/http://mattari-an.net/keyparty/bnrkp61.png",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "06_20160429185447_bnrkp62.png",
                [
                    Source(
                        "https://web.archive.org/web/20160429185447/http://mattari-an.net/keyparty/bnrkp62.png",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "06_20160429173149_bnrkp63.png",
                [
                    Source(
                        "https://web.archive.org/web/20160429173149/http://mattari-an.net/keyparty/bnrkp63.png",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "06_20160429173205_bnrkp64.png",
                [
                    Source(
                        "https://web.archive.org/web/20160429173205/http://mattari-an.net/keyparty/bnrkp64.png",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1313699, 136.8980176),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場　白鳥ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20260417110414/https://mattari-an.net/keyparty/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
                url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
            ),
        ]
        event = Event(
            aliases=["Keyパーティー6", "Key Party 6"],
            dates="2014.09.21",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20260417110414/https://mattari-an.net/keyparty/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20260609183908/http://mattari-an.net/keyparty/list.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2025.10.26",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =   # ==== keyparty ====
    # if i not in disabled_events:
    #     event_name = f"keyparty{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=[f"{i}"],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source(f"Date: {}", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         # last_edited="2025.10.25",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    media = [
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
    ]
    links = ["https://mattari-an.net/keyparty/", "https://x.com/key_party_abss"]

    event_group = EventGroup(
        aliases=[
            "Keyパーティー",
            "Key Party",
        ],
        events=events,
        media=media,
        links=links,
        sources=[
            # Source(
            #     "",
            #     (ReliabilityTypes.Reliable, OriginTypes.Official),
            # ),
        ],
        comments=None,
        description=None,
        last_edited="2026.10.26",
    )

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
