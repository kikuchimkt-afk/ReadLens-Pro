# -*- coding: utf-8 -*-
# Part1: Passages for Section 8
import json

def get_passages():
    return [
        {"id":"opinions","title":{"en":"[Step 1] Read a range of opinions","ja":"［ステップ1］幅広い意見を読む"},
         "layout":"speaker_boxes",
         "inline_solve_markers":[
             {"after_paragraph":4,"question_ids":["問1","問2"],"answer_numbers":[38,39]},
             {"after_paragraph":4,"marker_type":"navigate","action_ja":"解答が終わったら本文に戻り、Step 2 に進みます。"}
         ],
         "paragraphs":[
            [{"id":"s8_apu_h","en":"Apu (university professor)","ja":"Apu（大学教授）"},
             {"id":"s8_s2","en":"The exploration of space requires a lot of research time and money.","ja":"宇宙の探検には多くの研究時間とお金が必要です。"},
             {"id":"s8_s3","en":"All this research has led to many new inventions and boosted humanity's scientific and technical knowledge.","ja":"こういった研究はすべて，多くの新しい発明をもたらし，人類の科学及び技術の知識を増進してきました。"},
             {"id":"s8_s4","en":"While laser eye surgery, solar cells, freeze-dried food, and wireless headsets are just a few examples that have come out of space research, perhaps the invention that has proven the most useful in modern life is the computer mouse.","ja":"目のレーザー手術，太陽電池，フリーズドライ食品，ワイヤレスヘッドセットは，宇宙研究から生まれてきたもののほんの数例にすぎませんが，現代生活の中で最も役立つことになった発明品は，コンピュータのマウスかもしれません。"},
             {"id":"s8_s5","en":"This was developed in the 1960s on a NASA research project.","ja":"これは1960年代にNASAの研究プロジェクトで開発されました。"}],
            [{"id":"s8_chr_h","en":"Christine (company CEO)","ja":"Christine（企業のCEO）"},
             {"id":"s8_s7","en":"Much space exploration relies on international cooperation, a good example being the International Space Station, launched in 1998.","ja":"宇宙探検の多くは国際協力に依存していて，良い例が1998年に打ち上げられた国際宇宙ステーションです。"},
             {"id":"s8_s8","en":"The main reasons for this cooperation are to share the huge costs involved and to improve national prestige.","ja":"こういった協力の主な理由は，必要となる巨額な費用を分担すること，そして国家の威信を高めることです。"},
             {"id":"s8_s9","en":"More recently, private companies have begun exploring space, though mostly for commercial reasons.","ja":"より最近になって，民間企業が宇宙探検を始めました。ただしこれは主に商業的な理由によるものです。"},
             {"id":"s8_s10","en":"In the future, it is possible that countries or corporations will try to colonize parts of the moon or Mars.","ja":"将来は，国や大企業が月や火星の一部に植民地を建設しようとする可能性もあります。"},
             {"id":"s8_s11","en":"While financial cooperation and raising prestige are welcome, improper commercial or military use of outer space is not.","ja":"資金面で協力したり威信を高めるのは喜ぶべきことですが，商業的・軍事的に宇宙空間を不適切に利用することは喜べません。"}],
            [{"id":"s8_mei_h","en":"Meilin (journalist)","ja":"Meilin（ジャーナリスト）"},
             {"id":"s8_s13","en":"As the famous physicist, Stephen Hawking, once said, it is probably dangerous to broadcast into deep space evidence of the existence of humans here on Earth.","ja":"有名な物理学者スティーブン・ホーキングがかつて言ったように，この地球上における人類の存在の証拠を遠い宇宙にまで知らしめるのはおそらく危険でしょう。"},
             {"id":"s8_s14","en":"If our nearest intelligent aliens are anything like us, then they will seek to conquer Earth and humanity.","ja":"もし私たちに最も近いところにいる知的な異星人が私たちに少しでも似ていたら，彼らは地球と人類の征服を目指すでしょう。"},
             {"id":"s8_s15","en":"For me, this is the greatest threat associated with space exploration.","ja":"私にとって，これは宇宙探検と結びつく最大の脅威です。"},
             {"id":"s8_s16","en":"The deeper into space we travel, the greater the likelihood Earth will be discovered by an aggressive alien civilization.","ja":"宇宙の深淵に入っていけばいくほど，地球が攻撃的な異星人の文明に発見される可能性が高まるのです。"}],
            [{"id":"s8_nao_h","en":"Naomi (lawyer)","ja":"Naomi（弁護士）"},
             {"id":"s8_s18","en":"Historically, jobs working at sea were likely the least safe, with the highest rates of death in the workplace.","ja":"歴史的に見ると，海へ出る仕事がおそらく最も安全度が低く，仕事場で死亡する率が最も高いものでした。"},
             {"id":"s8_s19","en":"In modern times, space is no different, if not worse.","ja":"現代では，宇宙はそれより悪くはないにしても，同じくらい危険です。"},
             {"id":"s8_s20","en":"Once we are just 10,000 meters or so above the surface of the Earth, there is little oxygen and the temperature is too low for human survival.","ja":"地表から1万メートルほど上昇するだけで，酸素はほとんどなく，気温も人間が生きていくには低すぎます。"},
             {"id":"s8_s21","en":"Since the first person went into space in 1961, 19 of 652 astronauts have died on the job: a fatality rate of 2.9%.","ja":"1961年に人間が最初に宇宙に行って以来，652人の宇宙飛行士のうち19人が任務中に亡くなりました。2.9パーセントの死亡率です。"},
             {"id":"s8_s22","en":"No other business or industry would tolerate such a high level of danger. Why should the space industry?","ja":"このような危険度の高さを容認するビジネスや産業は他にありません。なぜ宇宙産業だけが例外なのでしょうか？"}],
            [{"id":"s8_vic_h","en":"Victor (financial analyst)","ja":"Victor（財政アナリスト）"},
             {"id":"s8_s24","en":"Space exploration has contributed hugely to economic growth.","ja":"宇宙探検は経済成長に大きく貢献してきました。"},
             {"id":"s8_s25","en":"In the USA, NASA provided work for nearly 340,000 people in 2021, mostly at above-average salaries, and it is estimated that it has contributed $7.7 billion in taxes to the US government.","ja":"米国では，2021年にNASAが34万人近くに仕事を提供しましたが，そのほとんどが平均給与を上回っていて，それは77億ドルもの税収を米国政府にもたらしたと見積もられています。"},
             {"id":"s8_s26","en":"Space is also being explored by other countries, such as China, India, Japan, and Russia.","ja":"宇宙の探検は，中国，インド，日本，ロシアなど他の国々も行っています。"},
             {"id":"s8_s27","en":"In the future, further economic growth will be ensured by more private firms entering the space race and by the rise of space tourism, space mining, space colonization, and space militarization.","ja":"将来は，より多くの民間会社が宇宙競争に参加し，宇宙旅行，宇宙での資源採掘，宇宙の植民地化，宇宙の軍事化が増加することにより，さらなる経済成長が確実となるでしょう。"}]
        ]},
        {"id":"position","title":{"en":"[Step 2] Take a position","ja":"［ステップ2］見解を固める"},
         "inline_solve_markers":[
             {"after_paragraph":0,"question_ids":["問3"],"answer_numbers":[40,41,42]},
             {"after_paragraph":0,"marker_type":"navigate","action_ja":"解答が終わったら本文に戻り、Step 3 のアウトラインへ進みます。"}
         ],
         "paragraphs":[[
             {"id":"s8_s28","en":"Now that you have understood the various opinions, you have taken a position on space exploration and written some notes below.","ja":"あなたはいろいろな意見を理解したので，宇宙探検についての見解を固めて，下のようなメモを作成した。"},
             {"id":"s8_s29","en":"POSITION: Space exploration is not a good idea.","ja":"見解：宇宙探検は勧められない。"},
             {"id":"s8_s30","en":"[40] and [41] opinions support this the most.","ja":"[40]意見と[41]意見がこれを最も支持している。"},
             {"id":"s8_s31","en":"An argument common to these two people is that [42].","ja":"この2人に共通する主張は，[42]ということである。"}
        ]]},
        {"id":"outline","title":{"en":"[Step 3] Create an outline of your essay","ja":"［ステップ3］エッセイのアウトラインを作成する"},
         "paragraphs":[
            [{"id":"s8_s32","en":"A Reconsideration of Space Exploration","ja":"宇宙探検の見直し"},
             {"id":"s8_s33","en":"Introduction","ja":"序論"},
             {"id":"s8_s34","en":"Space exploration is without doubt on the frontline of science, but it should not be a priority for the following three reasons.","ja":"宇宙探検が科学の最先端であることに疑いはないが，次の3つの理由により，それを優先事項にするべきではない。"}],
            [{"id":"s8_s35","en":"Body","ja":"本論"},
             {"id":"s8_s36","en":"REASON 1 from Step 2, based on evidence from the opinions in Step 1","ja":"理由1　ステップ2から。ステップ1の意見からの根拠に基づいて"},
             {"id":"s8_s37","en":"REASON 2 ([43]), based on evidence from Source A","ja":"理由2（[43]）。資料Aからの根拠に基づいて"},
             {"id":"s8_s38","en":"REASON 3, based on evidence ([44]) from Source B","ja":"理由3　資料Bからの根拠（[44]）に基づいて"}],
            [{"id":"s8_s39","en":"Conclusion","ja":"結論"},
             {"id":"s8_s40","en":"Upon consideration of all its aspects, we should perhaps prioritize other things over exploring space.","ja":"すべての面を考慮に入れると，宇宙探検以外の物事を優先する方が良いかもしれない。"}]
        ]},
        {"id":"source_a","title":{"en":"Source A","ja":"資料A"},
         "inline_solve_markers":[
             {"after_paragraph":0,"question_ids":["問4"],"answer_numbers":[43]},
             {"after_paragraph":0,"marker_type":"navigate","action_ja":"解答が終わったら本文に戻り、資料Bを読みます。"}
         ],
         "paragraphs":[[
             {"id":"s8_s41","en":"Although you may not make a direct connection between space exploration and environmental problems, a connection does exist.","ja":"宇宙探検と環境問題を直接関係づけることはないかもしれませんが，関係は確かにあるのです。"},
             {"id":"s8_s42","en":"First, the CO2 emissions of spacecraft are not insignificant.","ja":"第1に，宇宙船のCO2排出量は看過できません。"},
             {"id":"s8_s43","en":"It is estimated that one spacecraft launch emits 200-300 tons of CO2 and other harmful gases into the Earth's atmosphere.","ja":"宇宙船を1回打ち上げると，200から300トンのCO2及びその他の有害ガスが地球の大気中に放出されると見積もられています。"},
             {"id":"s8_s44","en":"More and more spacecraft are being sent into space, which is damaging for the Earth.","ja":"ますます多くの宇宙船が宇宙に送り出されており，これは地球にダメージを与えます。"},
             {"id":"s8_s45","en":"The contribution to the greenhouse effect of these craft's CO2 emissions is causing the Earth's temperature to rise.","ja":"これらの宇宙船のCO2排出量が温室効果の一因となっていることにより，地球の温度が上昇しています。"},
             {"id":"s8_s46","en":"Second, space exploration is damaging the thermosphere (the space environment close to the Earth).","ja":"第2に，宇宙探検は熱圏（地球に近い宇宙環境）にダメージを与えています。"},
             {"id":"s8_s47","en":"The quantity of space debris, the junked parts of spacecraft or artificial satellites, is on the rise.","ja":"宇宙船や人工衛星の残骸である宇宙ゴミの量も増加しています。"},
             {"id":"s8_s48","en":"NASA estimates that, in the thermosphere, there are currently around 23,000 pieces of space debris which are larger than a softball and travel at speeds of up to 28,000 km/h.","ja":"NASAの見積もりによると，現在熱圏にはソフトボールよりも大きい宇宙ゴミが約23,000片もあり，時速最大28,000キロで飛交っています。"},
             {"id":"s8_s49","en":"This poses a risk to future spaceflight, and may even be a potential obstacle to astronomical observation.","ja":"これは将来の宇宙飛行に危険を及ぼし，天体観測への潜在的な障害となる恐れさえあるのです。"}
        ]]},
        {"id":"source_b","title":{"en":"Source B","ja":"資料B"},
         "inline_solve_markers":[
             {"after_paragraph":0,"question_ids":["問5"],"answer_numbers":[44]}
         ],
         "graph_image":{"src":"source_b_graph.png","alt":"Government investment vs. potential annual budgets","after_paragraph":1},
         "paragraphs":[[
             {"id":"s8_s50","en":"Space exploration is getting more and more costly; in 2022 it was reported that the total amount of money spent by all the governments around the world was more than US$100 billion.","ja":"宇宙探検にはますますお金がかかるようになっています。2022年の報告によると，世界の全政府が使ったお金の合計額は，1千億米ドル超でした。"},
             {"id":"s8_s51","en":"The graph below compares this cost with the annual budgets, estimated by international institutions, that would be required to address some of the world's most important issues.","ja":"下のグラフはこの費用を，世界の最も重要な問題のいくつかに取り組むために必要となる年間予算の見込みと比較したもので，予算は国際機関の見積もりによるものです。"}
         ]]}
    ]

if __name__=='__main__':
    print(json.dumps(get_passages(),ensure_ascii=False,indent=2)[:200])
    print('passages OK, count:',len(get_passages()))
