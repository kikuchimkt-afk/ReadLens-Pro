import json
import os

def build_section01():
    return {
        "section_number": 1,
        "title": "第1問",
        "points": 10,
        "points_per_question": 2,
        "subsections": [
            {
                "label": "A",
                "situation": {
                    "en": "You are studying English at a language school in the US. The school is planning an event. You want to attend, so you are reading the flyer.",
                    "ja": "あなたは米国のある語学学校で英語を学んでいます。学校はあるイベントを計画中です。あなたは参加したいので、案内広告を読んでいます。"
                },
                "passages": [
                    {
                        "id": "header_1a",
                        "no_divider": True,
                        "title": {
                            "en": "The Thorpe English Language School\nInternational Night",
                            "ja": "ソープ英語学校\nインターナショナルな夕べ"
                        },
                        "subtitle": {
                            "en": "Friday, May 24, 5 p.m.-8 p.m.\nEntrance Fee: $5",
                            "ja": "5月24日金曜日 午後5時から8時\n入場料：5ドル"
                        }
                    },
                    {
                        "id": "intro_1a",
                        "no_divider": True,
                        "sentences": [
                            {
                                "id": "1a_s1",
                                "en": "The Thorpe English Language School (TELS) is organizing an international exchange event.",
                                "ja": "ソープ英語学校(TELS)はインターナショナルな交流イベントを計画しています。"
                            },
                            {
                                "id": "1a_s2",
                                "en": "TELS students don't need to pay the entrance fee.",
                                "ja": "TELSの学生は入場料を支払う必要はありません。"
                            },
                            {
                                "id": "1a_s3",
                                "en": "Please present your student ID at the reception desk in the Student Lobby.",
                                "ja": "学生ロビーの受付で学生証を提示してください。"
                            }
                        ]
                    },
                    {
                        "id": "foods_1a",
                        "no_divider": True,
                        "title": {
                            "en": "● Enjoy foods from various parts of the world",
                            "ja": "● 世界の様々な地域の食べ物を味わおう"
                        },
                        "sentences": [
                            {
                                "id": "1a_s4",
                                "en": "Have you ever tasted hummus from the Middle East?",
                                "ja": "中東のフムスの味をご存知ですか？"
                            },
                            {
                                "id": "1a_s5",
                                "en": "How about tacos from Mexico? Couscous from North Africa? Try them all!",
                                "ja": "メキシコのタコスはどうですか？ 北アフリカのクスクスは？ すべて試食できますよ。"
                            }
                        ]
                    },
                    {
                        "id": "languages_1a",
                        "no_divider": True,
                        "title": {
                            "en": "● Experience different languages and new ways to communicate",
                            "ja": "● 色々な言語や新しいコミュニケーションの仕方を体験しよう"
                        },
                        "sentences": [
                            {
                                "id": "1a_s6",
                                "en": "Write basic expressions such as \"hello\" and \"thank you\" in Arabic, Italian, Japanese, and Spanish.",
                                "ja": "\"hello\"や\"thank you\"などの基本的な表現をアラビア語、イタリア語、日本語、スペイン語で書いてみましょう。"
                            },
                            {
                                "id": "1a_s7",
                                "en": "Learn how people from these cultures use facial expressions and their hands to communicate.",
                                "ja": "こういった文化圏の人々がコミュニケーションをとるために、表情や手をどのように用いるのかを学びましょう。"
                            }
                        ]
                    },
                    {
                        "id": "dance_1a",
                        "no_divider": True,
                        "title": {
                            "en": "● Watch dance performances",
                            "ja": "● ダンスの実演を見学しよう"
                        },
                        "image": {
                            "src": "data/kakomon/2024/images/s1a_hula_dancer.png",
                            "alt": "Hula dancer illustration",
                            "float": "right"
                        },
                        "sentences": [
                            {
                                "id": "1a_s8",
                                "en": "From 7 p.m. watch flamenco, hula, and samba dance shows on the stage!",
                                "ja": "午後7時から舞台で行われるフラメンコ、フラダンス、サンバのダンスショーを見てください！"
                            },
                            {
                                "id": "1a_s9",
                                "en": "After each dance, performers will teach some basic steps. Please join in.",
                                "ja": "それぞれのダンスの後で、実演者が基本のステップを教えます。どうぞ参加してください。"
                            }
                        ]
                    },
                    {
                        "id": "footer_1a",
                        "no_divider": True,
                        "sentences": [
                            {
                                "id": "1a_s10",
                                "en": "Lots of pictures, flags, maps, textiles, crafts, and games will be displayed in the hall.",
                                "ja": "ホールでは、たくさんの写真、旗、地図、織物、手工芸品、ゲームが展示されます。"
                            },
                            {
                                "id": "1a_s11",
                                "en": "If you have some pictures or items from your home country which can be displayed at the event, let a school staff member know by May 17!",
                                "ja": "あなたの出身国の写真や物品で、イベントで展示できるものをお持ちでしたら、5月17日までに学校職員にお知らせくださいね！"
                            }
                        ]
                    }
                ],
                "questions": [
                    {
                        "question_id": "問1",
                        "answer_number": 1,
                        "stem": {
                            "en": "To join the event free of charge, you must [1].",
                            "ja": "「このイベントに無料で参加するには、[1]しなければならない。」"
                        },
                        "choices": [
                            {"label": "①", "en": "bring pictures from your home country", "ja": "出身国の写真を持参"},
                            {"label": "②", "en": "consult a staff member about the display", "ja": "ショーのことでスタッフに相談する"},
                            {"label": "③", "en": "fill out a form in the Student Lobby", "ja": "学生ロビーにある用紙に記入"},
                            {"label": "④", "en": "show proof that you are a TELS student", "ja": "TELSの学生であることを証明するものを提示"}
                        ],
                        "answer": 4,
                        "explanation": {
                            "ja": "正解は④。案内広告の「TELS students don't need to pay the entrance fee. Please present your student ID...」から、TELSの学生であることを証明するもの（学生証）を提示する必要があるとわかる。"
                        }
                    },
                    {
                        "question_id": "問2",
                        "answer_number": 2,
                        "stem": {
                            "en": "At the event, you can [2].",
                            "ja": "「このイベントでは、[2]ことができる。」"
                        },
                        "choices": [
                            {"label": "①", "en": "learn about gestures in various cultures", "ja": "様々な文化のジェスチャーを学ぶ"},
                            {"label": "②", "en": "participate in a dance competition", "ja": "ダンス競技会に参加する"},
                            {"label": "③", "en": "read short stories in foreign languages", "ja": "外国語で短い物語を読む"},
                            {"label": "④", "en": "try cooking international dishes", "ja": "国際的な料理を作ってみる"}
                        ],
                        "answer": 1,
                        "explanation": {
                            "ja": "正解は①。「Experience different languages...」のセクションに「Learn how people from these cultures use facial expressions and their hands to communicate.（表情や手をどのように用いるのかを学びましょう）」とあり、ジェスチャーを学べる内容と一致する。"
                        }
                    }
                ]
            },
            {
                "label": "B",
                "situation": {
                    "en": "You are an exchange student in the US and next week your class will go on a day trip. The teacher has provided some information.",
                    "ja": "あなたは米国にいる交換留学生で、来週あなたのクラスは日帰り旅行に出かけます。先生が情報を提供してくれました。"
                },
                "passages": [
                    {
                        "id": "header_1b",
                        "title": {
                            "en": "Tours of Yentonville",
                            "ja": "イエントンビルのツアー"
                        },
                        "subtitle": {
                            "en": "The Yentonville Tourist Office offers three city tours.",
                            "ja": "イエントンビル旅行案内所は、3つの市内観光ツアーを提供しています。"
                        }
                    },
                    {
                        "id": "history_tour",
                        "title": {
                            "en": "The History Tour",
                            "ja": "歴史ツアー"
                        },
                        "image": {
                            "src": "data/kakomon/2024/images/s1b_mayors_house.png",
                            "alt": "Mayor's House illustration",
                            "float": "right"
                        },
                        "sentences": [
                            {
                                "id": "1b_s1",
                                "en": "The day will begin with a visit to St. Patrick's Church, which was built when the city was established in the mid-1800s.",
                                "ja": "ツアーの1日は、聖パトリック教会の訪問から始まります。この教会は1800年代の半ばに市が設立された時に建てられたものです。"
                            },
                            {
                                "id": "1b_s2",
                                "en": "Opposite the church is the early-20th-century Mayor's House.",
                                "ja": "教会の向かい側には、20世紀初めの市長舎があります。"
                            },
                            {
                                "id": "1b_s3",
                                "en": "There will be a tour of the house and its beautiful garden.",
                                "ja": "市長舎とその美しい庭園のツアーが行われます。"
                            },
                            {
                                "id": "1b_s4",
                                "en": "Finally, cross the city by public bus and visit the Peace Park.",
                                "ja": "最後に、公共バスで市を横断して、平和公園を訪れましょう。"
                            },
                            {
                                "id": "1b_s5",
                                "en": "Opened soon after World War II, it was the site of many demonstrations in the 1960s.",
                                "ja": "ここは第二次世界大戦のすぐ後に開園し、1960年代にはここで数多くのデモ活動が行われました。"
                            }
                        ]
                    },
                    {
                        "id": "arts_tour",
                        "title": {
                            "en": "The Arts Tour",
                            "ja": "芸術ツアー"
                        },
                        "image": {
                            "src": "data/kakomon/2024/images/s1b_artist.png",
                            "alt": "Artist painting illustration",
                            "float": "left"
                        },
                        "sentences": [
                            {
                                "id": "1b_s6",
                                "en": "The morning will be spent in the Yentonville Arts District.",
                                "ja": "午前中はイエントンビル芸術地区で過ごします。"
                            },
                            {
                                "id": "1b_s7",
                                "en": "We will begin in the Art Gallery where there are many paintings from Europe and the US.",
                                "ja": "最初に訪れるのは、数多くのヨーロッパや米国の絵画がある美術館です。"
                            },
                            {
                                "id": "1b_s8",
                                "en": "After lunch, enjoy a concert across the street at the Bruton Concert Hall before walking a short distance to the Artists' Avenue.",
                                "ja": "昼食後は通りの向かい側に行き、ブルートン音楽堂でコンサートを楽しんでから、少し歩いて芸術家通りに行きます。"
                            },
                            {
                                "id": "1b_s9",
                                "en": "This part of the district was developed several years ago when new artists' studios and the nearby Sculpture Park were created.",
                                "ja": "この区域は数年前、新しい芸術家たちのアトリエと近隣にある彫刻公園が造られた時に開発されました。"
                            },
                            {
                                "id": "1b_s10",
                                "en": "Watch artists at work in their studios and afterwards wander around the park, finding sculptures among the trees.",
                                "ja": "芸術家たちのアトリエでの制作活動を見た後は、公園を散策して、木々の中に彫刻を見つけてください。"
                            }
                        ]
                    },
                    {
                        "id": "sports_tour",
                        "title": {
                            "en": "The Sports Tour",
                            "ja": "スポーツツアー"
                        },
                        "image": {
                            "src": "data/kakomon/2024/images/s1b_hockey_player.png",
                            "alt": "Hockey player illustration",
                            "float": "right"
                        },
                        "sentences": [
                            {
                                "id": "1b_s11",
                                "en": "First thing in the morning, you can watch the Yentonville Lions football team training at their open-air facility in the suburbs.",
                                "ja": "朝一番で、イエントンビル・ライオンズというフットボールチームがトレーニングしているのを、郊外にある屋外施設で見学できます。"
                            },
                            {
                                "id": "1b_s12",
                                "en": "In the afternoon, travel by subway to the Yentonville Hockey Arena, completed last fall.",
                                "ja": "午後は、昨秋に完成したイエントンビルホッケー競技場まで地下鉄で移動します。"
                            },
                            {
                                "id": "1b_s13",
                                "en": "Spend some time in its exhibition hall to learn about the arena's unique design.",
                                "ja": "この競技場の独特のデザインについて知るために、展示ホールでしばらく時間を過ごしてください。"
                            },
                            {
                                "id": "1b_s14",
                                "en": "Finally, enjoy a professional hockey game in the arena.",
                                "ja": "最後に、競技場でプロによるホッケーの試合を楽しみましょう。"
                            }
                        ]
                    },
                    {
                        "id": "footer_1b",
                        "sentences": [
                            {
                                "id": "1b_s15",
                                "en": "Yentonville Tourist Office, January, 2024",
                                "ja": "2024年1月、イエントンビル旅行案内所"
                            }
                        ]
                    }
                ],
                "questions": [
                    {
                        "question_id": "問1",
                        "answer_number": 3,
                        "stem": {
                            "en": "Yentonville has [3].",
                            "ja": "「イエントンビルには[3]がある。」"
                        },
                        "choices": [
                            {"label": "①", "en": "a church built 250 years ago when the city was constructed", "ja": "市が建設された250年前に建てられた教会"},
                            {"label": "②", "en": "a unique football training facility in the center of the town", "ja": "町の中心部にある独特なフットボールのトレーニング施設"},
                            {"label": "③", "en": "an art studio where visitors can create original works of art", "ja": "訪問客が独自の芸術作品を作ることができるアトリエ"},
                            {"label": "④", "en": "an arts area with both an art gallery and a concert hall", "ja": "美術館と音楽堂の両方がある芸術地区"}
                        ],
                        "answer": 4,
                        "explanation": {
                            "ja": "正解は④。The Arts Tour に「We will begin in the Art Gallery... enjoy a concert across the street at the Bruton Concert Hall...」とあることから、美術館と音楽堂の両方があることがわかる。"
                        }
                    },
                    {
                        "question_id": "問2",
                        "answer_number": 4,
                        "stem": {
                            "en": "On all three tours, you will [4].",
                            "ja": "「3つのツアーすべてにおいて、あなたは[4]だろう。」"
                        },
                        "choices": [
                            {"label": "①", "en": "learn about historic events in the city", "ja": "市の歴史的な事件について学ぶ"},
                            {"label": "②", "en": "see people demonstrate their skills", "ja": "人々が自分の技術を披露しているのを見る"},
                            {"label": "③", "en": "spend time both indoors and outdoors", "ja": "屋内と屋外の両方で時間を過ごす"},
                            {"label": "④", "en": "use public transportation to get around", "ja": "公共交通を利用して動き回る"}
                        ],
                        "answer": 3,
                        "explanation": {
                            "ja": "正解は③。各ツアーには、教会の訪問や美術館などの屋内での活動と、公園や屋外施設などの屋外での活動がそれぞれ含まれているため、3つのツアーすべてで屋内と屋外の両方で時間を過ごすことになる。"
                        }
                    },
                    {
                        "question_id": "問3",
                        "answer_number": 5,
                        "stem": {
                            "en": "Which is the newest place in Yentonville you can visit on the tours?",
                            "ja": "「ツアーで訪れることのできる、イエントンビルの中の最も新しい場所はどれか。」"
                        },
                        "choices": [
                            {"label": "①", "en": "The Hockey Arena", "ja": "ホッケー競技場"},
                            {"label": "②", "en": "The Mayor's House", "ja": "市長舎"},
                            {"label": "③", "en": "The Peace Park", "ja": "平和公園"},
                            {"label": "④", "en": "The Sculpture Park", "ja": "彫刻公園"}
                        ],
                        "answer": 1,
                        "explanation": {
                            "ja": "正解は①。スポーツツアーの項に「the Yentonville Hockey Arena, completed last fall（昨秋に完成したイエントンビルホッケー競技場）」とあり、他の場所よりも明らかに新しく造られたものである。"
                        }
                    }
                ]
            }
        ]
    }

def main():
    json_path = os.path.join(os.path.dirname(__file__), 'data.json')
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {"exam_info": {}, "sections": []}
    
    sec01 = build_section01()
    
    # 既存の第1問があれば削除して差し替え
    data['sections'] = [s for s in data.get('sections', []) if s.get('section_number') != 1]
    data['sections'].append(sec01)
    
    if 1 not in data['exam_info'].get('implemented_sections', []):
        data['exam_info'].setdefault('implemented_sections', []).append(1)
        data['exam_info']['implemented_sections'].sort()

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Section 1 added successfully!")

if __name__ == '__main__':
    main()
