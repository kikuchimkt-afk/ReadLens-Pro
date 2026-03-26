import json
import re

en_text = """
Ice hockey is a team sport enjoyed by a wide variety of people around the world. The object of the sport is to move a hard rubber disk called a "puck" into the other team's net with a hockey stick. Two teams with six players on each team engage in this fast-paced sport on a hard and slippery ice rink. Players may reach a speed of 30 kilometers per hour sending the puck into the air. At this pace, both the players and the puck can be a cause of serious danger.
The speed of the sport and the slippery surface of the ice rink make it easy for players to fall down or bump into each other resulting in a variety of injuries. In an attempt to protect players, equipment such as helmets, gloves, and pads for the shoulders, elbows, and legs, has been introduced over the years. Despite these efforts, ice hockey has a high rate of concussions.
A concussion is an injury to the brain that affects the way it functions; it is caused by either direct or indirect impact to the head, face, neck, or elsewhere and can sometimes cause temporary loss of consciousness. In less serious cases, for a short time, players may be unable to walk straight or see clearly, or they may experience ringing in the ears. Some believe they just have a slight headache and do not realize they have injured their brains.
In addition to not realizing the seriousness of the injury, players tend to worry about what their coach will think. In the past, coaches preferred tough players who played in spite of the pain. In other words, while it would seem logical for an injured player to stop playing after getting hurt, many did not. Recently, however, it has been found that concussions can have serious effects that last a lifetime. People with a history of concussion may have trouble concentrating or sleeping. Moreover, they may suffer from psychological problems such as depression and mood changes. In some cases, players may develop smell and taste disorders.
The National Hockey League (NHL), consisting of teams in Canada and the United States, has been making stricter rules and guidelines to deal with concussions. For example, in 2001, the NHL introduced the wearing of visors—pieces of clear plastic attached to the helmet that protect the face. At first, it was optional and many players chose not to wear them. Since 2013, however, it has been required. In addition, in 2004, the NHL began to give more severe penalties, such as suspensions and fines, to players who hit another player in the head deliberately.
The NHL also introduced a concussion spotters system in 2015. In this system, NHL officials with access to live streaming and video replay watch for visible indications of concussion during each game. At first, two concussion spotters, who had no medical training, monitored the game in the arena. The following year, one to four concussion spotters with medical training were added. They monitored each game from the League's head office in New York. If a spotter thinks that a player has suffered a concussion, the player is removed from the game and is taken to a "quiet room" for an examination by a medical doctor. The player is not allowed to return to the game until the doctor gives permission.
The NHL has made much progress in making ice hockey a safer sport. As more is learned about the causes and effects of concussions, the NHL will surely take further measures to ensure player safety. Better safety might lead to an increase in the number of ice hockey players and fans.
"""

ja_text = """
アイスホッケーは世界中でさまざまな人に楽しまれているチームスポーツだ。このスポーツの目的は，「パック」と呼ばれる硬いゴム製の円盤をホッケースティックで相手チームのネットに入れることだ。各チームに6人の選手がいる2つのチームが，硬くて滑りやすいアイスリンクでこのペースの速いスポーツをする。選手がパックを空中に打つ時，時速30キロに達することもある。この速度では，選手もパックも重大な危険の原因になる可能性があるのだ。
そのスポーツのスピードとアイスリンク表面の滑りやすさは，選手の転倒や，選手同士の衝突を容易に引き起こし，結果としていろいろなケガにつながる。長年にわたり，選手を守ろうとする試みにおいて，ヘルメット，グローブ，肩やひじや脚のパッドのような装備品が導入されてきている。しかしこのような努力にもかかわらず，アイスホッケーが脳しんとうにつながる確率は高い。
脳しんとうは，脳の機能に影響を与える脳の負傷だ。それは頭，顔，首などの部位への直接的または間接的な衝撃によって起こり，ときには一時的な意識喪失を起こすこともある。あまり深刻でない場合でも，短い時間，選手はまっすぐ歩けなかったり，はっきりと見えなくなったり，耳鳴りを経験することもある。選手の中には軽い頭痛だと思って，自分が脳を負傷していることに気づかない人もいる。
負傷の深刻さに気づかないことに加え，選手はコーチがどう思うかを心配する傾向にある。昔は，コーチは痛みにもかかわらずプレーするタフな選手をより好んだ。言い換えると，負傷した選手は負傷直後にプレーをやめるのが論理的であると思われるのに，多くはそうしなかったのだ。しかし最近，脳しんとうはその人の一生涯にわたって深刻な影響をおよぼす可能性があるとわかってきた。脳しんとうの病歴のある人は，集中力や睡眠に問題を抱えるかもしれないのだ。さらに，彼らはうつ病や情緒不安定のような精神的問題に苦しむかもしれないのだ。いくつかのケースでは，選手は嗅覚と味覚に障害を発症するかもしれないのだ。
カナダとアメリカのチームで構成されるナショナル・ホッケー・リーグ（NHL）は，脳しんとうに対処するためにより厳しいルールとガイドラインを作ってきた。たとえば，2001年，NHLはバイザー――つまりヘルメットに取りつけられた顔を保護する透明なプラスチック片を着用することを導入した。最初，それは任意で，多くの選手は着用しないことを選んだ。しかし2013年から，それは義務化された。加えて，2004年，NHLは故意に他の選手の頭部を殴打した選手に対し，出場停止や罰金などのより厳しいペナルティーを与え始めた。
2015年，NHLは脳しんとうスポッター（監視員）システムも導入した。このシステムは，ライブ配信やリプレイ映像にアクセスするNHLの公式スタッフが試合中に脳しんとうの見た目にわかる兆候を監視するのだ。最初は，医学的訓練を受けていない2人の脳しんとうスポッターがアリーナで試合を監視していた。その翌年，医療研修を受けた1〜4人の脳しんとうスポッターが追加された。彼らはニューヨークのリーグ本部オフィスから各試合を監視した。もしスポッターが，ある選手が脳しんとうを起こしているとみなすと，その選手は試合から外され，「安静室」に連れて行かれて医者の検査を受ける。医者が許可を出すまで，その選手は試合に戻ることを許されないのだ。
アイスホッケーをより安全なスポーツにすることにおいて，NHLは大きな進歩を成し遂げてきた。脳しんとうの原因や影響がより明らかになるにつれて，選手の安全を確実にするためにNHLがさらに対策を講じることは確かであろう。より高い安全性はアイスホッケー選手とファンの増加につながるであろう。
"""

en_paras = [p.strip() for p in en_text.strip().split('\n') if p.strip()]
ja_paras = [p.strip() for p in ja_text.strip().split('\n') if p.strip()]

paragraphs_out = []
sid = 1
for i, (ep, jp) in enumerate(zip(en_paras, ja_paras)):
    es = [s.strip() + '.' for s in ep.split('. ') if s.strip()]
    if es and es[-1].endswith('..'):
        es[-1] = es[-1][:-1]
    js = jp.replace('。', '。\n').replace('！', '！\n').replace('？', '？\n').split('\n')
    js = [s.strip() for s in js if s.strip()]
    
    if len(es) != len(js):
        print(f"Warning: Paragraph {i} mismatch. EN: {len(es)}, JA: {len(js)}")
        # Manual fix logic if needed, but assuming they match for now
        print(f"EN: {es}")
        print(f"JA: {js}")
        # let's map roughly
        if len(es) < len(js):
            js = js[:len(es)-1] + ["".join(js[len(es)-1:])]
        else:
            es = es[:len(js)-1] + ["".join(es[len(js)-1:])]
            
    p_out = []
    for eng, jpn in zip(es, js):
        p_out.append({
            "id": f"6a_s{sid}",
            "en": eng,
            "ja": jpn
        })
        sid += 1
    paragraphs_out.append(p_out)

sec6a = {
    "section_number": "6A",
    "title": "第6問 A",
    "points": 12,
    "pdf_pages": [28, 29, 30, 31],
    "passage_images": [
        "images/mondai_p28.png",
        "images/mondai_p29.png",
        "images/mondai_p30.png"
    ],
    "explanation_images": [
        "images/kaitou_p17.png",
        "images/kaitou_p18.png",
        "images/kaitou_p19.png"
    ],
    "situation": {
        "en": "You are working on a class project about safety in sports and found the following article. You are reading it and making a poster to present your findings to your classmates.",
        "ja": "あなたはスポーツの安全性に関するクラスのプロジェクトに取り組んでおり，次の記事を見つけました。あなたはそれを読み，クラスメートに気づいたことを伝えるためにポスターを作っています。"
    },
    "passages": [
        {
            "id": "article",
            "title": {
                "en": "Making Ice Hockey Safer",
                "ja": "アイスホッケーをもっと安全に"
            },
            "paragraphs": paragraphs_out
        },
        {
            "id": "notes",
            "title": {
                "en": "Your poster:",
                "ja": "あなたのポスター："
            },
            "type": "handout",
            "paragraphs": [
                [
                    {
                        "id": "6a_s_p1",
                        "en": "Making Ice Hockey Safer",
                        "ja": "アイスホッケーをもっと安全に"
                    }
                ],
                [
                    {
                        "id": "6a_s_p2",
                        "en": "What is ice hockey?",
                        "ja": "アイスホッケーとは？"
                    },
                    {
                        "id": "6a_s_p3",
                        "en": "• Players score by putting a \"puck\" in the other team's net",
                        "ja": "• 選手が「パック」を相手チームのゴールネットに入れることで得点する。"
                    },
                    {
                        "id": "6a_s_p4",
                        "en": "• Six players on each team",
                        "ja": "• 各チーム6人"
                    },
                    {
                        "id": "6a_s_p5",
                        "en": "• Sport played on ice at a high speed",
                        "ja": "• 氷の上で高速でプレーされるスポーツ"
                    }
                ],
                [
                    {
                        "id": "6a_s_p6",
                        "en": "Main Problem: A High Rate of Concussions",
                        "ja": "主な問題：脳しんとうの高い発生率"
                    }
                ],
                [
                    {
                        "id": "6a_s_p7",
                        "en": "Definition of a concussion",
                        "ja": "脳しんとうの定義"
                    },
                    {
                        "id": "6a_s_p8",
                        "en": "An injury to the brain that affects the way it functions",
                        "ja": "脳の機能に影響を及ぼす脳の負傷"
                    }
                ],
                [
                    {
                        "id": "6a_s_p9",
                        "en": "Effects",
                        "ja": "脳しんとうの影響"
                    },
                    {
                        "id": "6a_s_p10",
                        "en": "Short-term\n• Loss of consciousness\n• Difficulty walking straight\n• [ 39 ]\n• Ringing in the ears",
                        "ja": "短期的\n• 意識の喪失\n• まっすぐ歩けない\n• [ 39 ]\n• 耳鳴り"
                    },
                    {
                        "id": "6a_s_p11",
                        "en": "Long-term\n• Problems with concentration\n• [ 40 ]\n• Psychological problems\n• Smell and taste disorders",
                        "ja": "長期的\n• 集中力の不足\n• [ 40 ]\n• 精神的な問題\n• 嗅覚と味覚の障害"
                    }
                ],
                [
                    {
                        "id": "6a_s_p12",
                        "en": "Solutions",
                        "ja": "解決策"
                    },
                    {
                        "id": "6a_s_p13",
                        "en": "National Hockey League (NHL)",
                        "ja": "ナショナル・ホッケー・リーグ（NHL）"
                    },
                    {
                        "id": "6a_s_p14",
                        "en": "• Requires helmets with visors",
                        "ja": "• バイザー付きヘルメット着用を義務づける"
                    },
                    {
                        "id": "6a_s_p15",
                        "en": "• Gives severe penalties to dangerous players",
                        "ja": "• 危険な選手に重いペナルティーを与える"
                    },
                    {
                        "id": "6a_s_p16",
                        "en": "• Has introduced concussion spotters to [ 41 ]",
                        "ja": "• [ 41 ] ために脳しんとうスポッターを導入した"
                    }
                ],
                [
                    {
                        "id": "6a_s_p17",
                        "en": "Summary",
                        "ja": "要約"
                    },
                    {
                        "id": "6a_s_p18",
                        "en": "Ice hockey players have a high risk of suffering from concussions. Therefore, the NHL has [ 42 ].",
                        "ja": "アイスホッケー選手は脳しんとうを起こす危険性が高い。それゆえ，NHLは [ 42 ]。"
                    }
                ]
            ]
        }
    ],
    "questions": [
        {
            "question_id": "問1",
            "answer_number": 39,
            "stem": {
                "en": "Choose the best option for [ 39 ] on your poster.",
                "ja": "「あなたのポスターの [ 39 ] に最も適する選択肢を選びなさい。」"
            },
            "choices": [
                {
                    "label": "①",
                    "en": "Aggressive behavior",
                    "ja": "攻撃的なふるまい",
                    "is_correct": False
                },
                {
                    "label": "②",
                    "en": "Difficulty thinking",
                    "ja": "思考困難",
                    "is_correct": False
                },
                {
                    "label": "③",
                    "en": "Personality changes",
                    "ja": "人格の変化",
                    "is_correct": False
                },
                {
                    "label": "④",
                    "en": "Unclear vision",
                    "ja": "視界不良",
                    "is_correct": True
                }
            ],
            "answer": "④",
            "explanation": {
                "ja": "[ 39 ] には，脳しんとうの短期的な影響が入る。本文第3段落第2文に，In less serious cases, for a short time, players may be unable to walk straight or see clearly... (あまり深刻でなくても，短い時間，選手はまっすぐ歩けなかったり，はっきりと見えなくなったり...) とあるので，unable to see clearly を unclear vision と言い換えた④が正解。①，②，③のような症状は本文に述べられていないので，不適当。",
                "evidence_sentences": ["6a_s10"]
            }
        },
        {
            "question_id": "問2",
            "answer_number": 40,
            "stem": {
                "en": "Choose the best option for [ 40 ] on your poster.",
                "ja": "「あなたのポスターの [ 40 ] に最も適する選択肢を選びなさい。」"
            },
            "choices": [
                {
                    "label": "①",
                    "en": "Loss of eyesight",
                    "ja": "視力の喪失",
                    "is_correct": False
                },
                {
                    "label": "②",
                    "en": "Memory problems",
                    "ja": "記憶障害",
                    "is_correct": False
                },
                {
                    "label": "③",
                    "en": "Sleep disorders",
                    "ja": "睡眠障害",
                    "is_correct": True
                },
                {
                    "label": "④",
                    "en": "Unsteady walking",
                    "ja": "歩行不安定",
                    "is_correct": False
                }
            ],
            "answer": "③",
            "explanation": {
                "ja": "[ 40 ] には，脳しんとうの長期的な影響が入る。第4段落第5文に，People with a history of concussion may have trouble concentrating or sleeping. (脳しんとうの病歴のある人は，集中力や睡眠に問題を抱えるかもしれないのだ。) とあるので，have trouble sleeping を sleep disorders と言い換えた③が正解。④の歩行不安定は，問1で見たように短期的な影響。したがって，④は不適当。①と②のような症状は本文で述べられていないので，不適当。",
                "evidence_sentences": ["6a_s18"]
            }
        },
        {
            "question_id": "問3",
            "answer_number": 41,
            "stem": {
                "en": "Choose the best option for [ 41 ] on your poster.",
                "ja": "「あなたのポスターの [ 41 ] に最も適する選択肢を選びなさい。」"
            },
            "choices": [
                {
                    "label": "①",
                    "en": "allow players to return to the game",
                    "ja": "選手が試合に戻ることを許可する",
                    "is_correct": False
                },
                {
                    "label": "②",
                    "en": "examine players who have a concussion",
                    "ja": "脳しんとうを起こしている選手を検査する",
                    "is_correct": False
                },
                {
                    "label": "③",
                    "en": "fine players who cause concussions",
                    "ja": "脳しんとうを起こしている選手に罰金を科す",
                    "is_correct": False
                },
                {
                    "label": "④",
                    "en": "identify players showing signs of a concussion",
                    "ja": "脳しんとうの兆候を示す選手を特定する",
                    "is_correct": True
                }
            ],
            "answer": "④",
            "explanation": {
                "ja": "[ 41 ] には，NHLが脳しんとうスポッター（監視員）を導入した目的が入る。脳しんとうスポッターの導入については，第6段落で述べられている。その役割については第6文に，If a spotter thinks that a player has suffered a concussion, the player is removed from the game and is taken to a \"quiet room\" for an examination by a medical doctor. (もしスポッターが，ある選手が脳しんとうを起こしているとみなすと，その選手は試合から除外され，「安静室」に連れて行かれて医者の検査を受ける。) と述べられている。したがって，④が正解。スポッターの役割は選手の特定のみで，検査をするのは医者なので，②は不適当。続く第7文に，The player is not allowed to return to the game until the doctor gives permission. (医者が許可を出すまで，その選手は試合に戻ることを許されないのだ。) とあり，選手が試合に戻る許可を与えるのはスポッターではなく，医者なので，①も不適当。第5段落最終文に，the NHL began to give more severe penalties, such as suspensions and fines, to players who hit another player in the head deliberately (NHLは故意にほかの選手の頭部を殴打した選手に対し，出場停止や罰金などのより厳しい罰を与えることを始めた) とあり，罰金を科されるのは脳しんとうを起こした選手ではなく，故意に危険なプレーをした選手なので，③も不適当。",
                "evidence_sentences": ["6a_s28", "6a_s29"]
            }
        },
        {
            "question_id": "問4",
            "answer_number": 42,
            "stem": {
                "en": "Choose the best option for [ 42 ] on your poster.",
                "ja": "「あなたのポスターの [ 42 ] に最も適する選択肢を選びなさい。」"
            },
            "choices": [
                {
                    "label": "①",
                    "en": "been expecting the players to become tougher",
                    "ja": "選手がもっとタフになることを期待し続けてきた",
                    "is_correct": False
                },
                {
                    "label": "②",
                    "en": "been implementing new rules and guidelines",
                    "ja": "新しい規則やガイドラインを施行し続けてきた",
                    "is_correct": True
                },
                {
                    "label": "③",
                    "en": "given medical training to coaches",
                    "ja": "コーチに医療研修をした",
                    "is_correct": False
                },
                {
                    "label": "④",
                    "en": "made wearing of visors optional",
                    "ja": "バイザーの着用を任意にした",
                    "is_correct": False
                }
            ],
            "answer": "②",
            "explanation": {
                "ja": "ポスターの該当箇所では，NHLが行ってきた脳しんとう対策を述べている。第5段落第1文に，The National Hockey League (NHL) ... has been making stricter rules and guidelines to deal with concussions. (ナショナル・ホッケー・リーグ（NHL）は，脳しんとうに対処するためにより厳しいルールとガイドラインを作ってきた。) とあり，その例として，第5段落ではバイザーとペナルティーの導入について，第6段落では脳しんとうスポッターの導入について述べている。したがって，②が正解。①については，第4段落第2文に，coaches preferred tough players who played in spite of the pain (コーチは痛みにもかかわらずプレーするタフな選手をより好んだ) とあり，選手がタフになるのを期待したのはNHLではなく，コーチだったので，不適当。③については，第6段落第4文に，one to four concussion spotters with medical training were added (医療研修を受けた1〜4人の脳しんとうスポッターが追加された) とあり，医療研修を受けたのは脳しんとうスポッターであり，コーチではないので，③も不適当。④については，第5段落第2〜4文ではバイザー導入について，「2001年のバイザー導入時は，着用は任意だったため，着用しない選手が多かったが，2013年からは着用が義務化された」と述べているので，④も不適当。",
                "evidence_sentences": ["6a_s21"]
            }
        }
    ]
}

with open(r"g:\マイドライブ\ReadLens Pro\data\kakomon\2021_1\sec6a.json", "w", encoding="utf-8") as f:
    json.dump(sec6a, f, ensure_ascii=False, indent=2)

print("Generated sec6a.json")
