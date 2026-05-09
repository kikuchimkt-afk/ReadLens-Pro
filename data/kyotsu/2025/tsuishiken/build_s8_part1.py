# -*- coding: utf-8 -*-
# Part1: Passages for Tsuishiken Section 8
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
            [{"id":"s8t_aya_h","en":"Aya (local government advisor)","ja":"Aya（地方自治体顧問）"},
             {"id":"s8t_s2","en":"In terms of their business practices, zoos are unusual in that, in principle, they don\u2019t buy animals.","ja":"ビジネスの手法に関しては，動物園は原則的に動物を買わないという点で独特です。"},
             {"id":"s8t_s3","en":"Apart from pandas, they only exchange them with other zoos.","ja":"パンダを除いて，動物は他の動物園と交換するのみです。"},
             {"id":"s8t_s4","en":"Nevertheless, zoos boost local economies: The money saved on not having to purchase their \u201cproduct\u201d can be used for employing staff, building zoo infrastructure, or running animal medical programs.","ja":"にもかかわらず，動物園は地域経済を押し上げます。「製品」を購入しなくてよいことから節約できるお金は，従業員の雇用，動物園のインフラ建設，動物の医療プログラムの実施などに使うことができます。"},
             {"id":"s8t_s5","en":"Other benefits provided by zoos include collaborating with universities on research, or with schools on children\u2019s education.","ja":"動物園が提供できるその他の利点には，大学との共同研究や，学校との連携による児童教育などがあります。"}],
            [{"id":"s8t_dav_h","en":"David (urban planner)","ja":"David（都市設計家）"},
             {"id":"s8t_s7","en":"Most zoos are located in urban areas, ensuring the business is economically viable because of the large population.","ja":"ほとんどの動物園は都市部にあって，人口が多いためにこのビジネスの経済的な存在は確保されています。"},
             {"id":"s8t_s8","en":"However, keeping dangerous and, in some cases, man-eating animals in the middle of a sea of humans can be a huge risk.","ja":"しかしながら，非常に多くの人間がいる中で危険な，場合によっては人間を食べる動物を飼うのは巨大なリスクになりうるのです。"},
             {"id":"s8t_s9","en":"In the country of Georgia, such animals as bears and lions recently escaped from Tbilisi Zoo after flooding, posing a danger to local citizens.","ja":"ジョージア国では，最近洪水の後でクマやライオンなどの動物がトビリシ動物園から逃げ出し，地元の市民に危険をもたらしました。"},
             {"id":"s8t_s10","en":"Perhaps we should close down zoos for safety reasons.","ja":"安全上の理由から動物園は閉鎖するのがよいかもしれません。"}],
            [{"id":"s8t_ind_h","en":"Indira (student)","ja":"Indira（学生）"},
             {"id":"s8t_s12","en":"Zoos are prisons for animals.","ja":"動物園は動物にとって監獄です。"},
             {"id":"s8t_s13","en":"Imagine being a cheetah, used to traveling long distances for food.","ja":"自分が食べ物を求めて長距離を移動することに慣れているチータになったと想像してみてください。"},
             {"id":"s8t_s14","en":"Then imagine being locked up for the rest of your life in a relatively small space, with no choice in your food, very little stimulation, and lots of strange, noisy humans looking at you every day.","ja":"次に死ぬまでずっと比較的小さな場所に閉じ込められて，食べる物を選ぶこともできず，刺激もほとんどなく，大勢の奇妙で騒々しい人間たちが毎日自分のことを見ていると想像してみてください。"},
             {"id":"s8t_s15","en":"We would not expose any persons to such cruel treatment.","ja":"私たちは人間をそんな残酷な目にあわせたりはしないでしょう。"},
             {"id":"s8t_s16","en":"Why do so many people think it\u2019s OK to treat animals in such a way?","ja":"なぜとても多くの人が動物をこんなふうに扱っても構わないと思っているのでしょうか？"}],
            [{"id":"s8t_ken_h","en":"Kenyatta (journalist)","ja":"Kenyatta（ジャーナリスト）"},
             {"id":"s8t_s18","en":"Zoos perform an important function in international relations.","ja":"動物園は国際関係において重要な機能を果たします。"},
             {"id":"s8t_s19","en":"China is well known for its \u201cpanda politics,\u201d whereby pandas are \u201cloaned\u201d to overseas zoos as a part of the country\u2019s \u201csoft power.\u201d","ja":"中国は「パンダ外交」を行っていることでも有名で，これによりパンダは，その「ソフトパワー」の一環として，海外の動物園に「貸与」されます。"},
             {"id":"s8t_s20","en":"Trade deals are often found where an animal is symbolic of a particular nation and is in high demand, like koalas and Australia.","ja":"コアラとオーストラリアのように，動物がある国を象徴して，とても人気がある場合には，貿易取引が頻繁に行われます。"},
             {"id":"s8t_s21","en":"Animals may be temporarily swapped between countries as part of a political treaty, in the same way as art galleries exchange paintings.","ja":"美術館が絵を交換するのと同じように，動物が政治協定の一部として一時的に国家間で交換されることもあります。"},
             {"id":"s8t_s22","en":"This can also help promote the mutual flow of zoological information that improves global connectivity.","ja":"これはまた，動物学上の情報のやり取りを促進するのにも役立ち，これによって世界全体のつながりがより良くなるのです。"}],
            [{"id":"s8t_yo_h","en":"Yo (office worker)","ja":"Yo（会社員）"},
             {"id":"s8t_s24","en":"One possible cause of pandemics is the migration of an animal virus to humans.","ja":"パンデミックの一因になりうるのは，動物ウイルスが人間に移ることです。"},
             {"id":"s8t_s25","en":"While so-called \u201cvirus jumping\u201d can happen in the wild, or at markets where live animals are sold, zoos too must be considered as a potential source of such events.","ja":"いわゆる「ウイルス・ジャンピング」は自然界，あるいは生きた動物が売られる市場で起こる可能性がありますが，動物園もこのような事態の潜在的な発生源の1つと考えなければなりません。"},
             {"id":"s8t_s26","en":"Given the loss of life and economic disruption that can be brought about by pandemics, governments around the world must guarantee that proper procedures are followed at zoos and safari parks in order to ensure such a leap between species cannot occur.","ja":"パンデミックがもたらすことのある人命の喪失や経済の混乱を考えた場合，このようにウイルスが異なる種に飛び移ることが絶対にないようにするため，世界各地の政府は動物園やサファリパークで適正な手続きが取られていることを保証しなければなりません。"}]
        ]},
        {"id":"position","title":{"en":"[Step 2] Take a position","ja":"［ステップ2］見解を固める"},
         "inline_solve_markers":[
             {"after_paragraph":0,"question_ids":["問3"],"answer_numbers":[40,41,42]},
             {"after_paragraph":0,"marker_type":"navigate","action_ja":"解答が終わったら本文に戻り、Step 3 のアウトラインへ進みます。"}
         ],
         "paragraphs":[[
             {"id":"s8t_s28","en":"Now that you have understood the various opinions, you have taken a position on zoos and written some notes below.","ja":"あなたはさまざまな意見を理解したので，動物園に関する見解を固めて，下にいくつかのメモを書いた。"},
             {"id":"s8t_s29","en":"POSITION: We should support and actively maintain zoos.","ja":"見解：私たちは動物園を支援して積極的に維持すべきだ。"},
             {"id":"s8t_s30","en":"[40] and [41] opinions support this the most.","ja":"[40]意見と[41]意見がこれを最も支持している。"},
             {"id":"s8t_s31","en":"An argument common to these two people is that [42].","ja":"この2人に共通する主張は，[42]ということである。"}
        ]]},
        {"id":"outline","title":{"en":"[Step 3] Create an outline of your essay","ja":"［ステップ3］エッセイのアウトラインを作成する"},
         "paragraphs":[
            [{"id":"s8t_s32","en":"We should support and actively maintain zoos","ja":"私たちは動物園を支援して積極的に維持すべきだ"},
             {"id":"s8t_s33","en":"Introduction","ja":"序論"},
             {"id":"s8t_s34","en":"Zoos offer many different benefits and should be viewed positively for the following three reasons.","ja":"動物園は種々さまざまな恩恵をもたらすので，次の3つの理由から肯定的に見るべきである。"}],
            [{"id":"s8t_s35","en":"Body","ja":"本論"},
             {"id":"s8t_s36","en":"REASON 1 from Step 2, based on evidence from the opinions in Step 1","ja":"理由1　ステップ2から，ステップ1の意見からの根拠に基づいて"},
             {"id":"s8t_s37","en":"REASON 2 ([43]), based on evidence from Source A","ja":"理由2（[43]），資料Aからの根拠に基づいて"},
             {"id":"s8t_s38","en":"REASON 3, based on evidence ([44]) from Source B","ja":"理由3　資料Bからの根拠（[44]）に基づいて"}],
            [{"id":"s8t_s39","en":"Conclusion","ja":"結論"},
             {"id":"s8t_s40","en":"We should continue to provide zoos with help and resources.","ja":"私たちは動物園に援助と財源を供給し続けるべきである。"}]
        ]},
        {"id":"source_a","title":{"en":"Source A","ja":"資料A"},
         "inline_solve_markers":[
             {"after_paragraph":0,"question_ids":["問4"],"answer_numbers":[43]},
             {"after_paragraph":0,"marker_type":"navigate","action_ja":"解答が終わったら本文に戻り、資料Bを読みます。"}
         ],
         "paragraphs":[[
             {"id":"s8t_s41","en":"According to the Red List published by the International Union for Conservation of Nature, more than 42,000 species were regarded as threatened with extinction in 2022, compared to approximately 24,000 in 2016.","ja":"国際自然保護連合が発表したレッドリストによると，絶滅の危機に瀕しているとみなされた種は，2016年はおよそ2万4千種だったのに対して，2022年には4万2千種を超えた。"},
             {"id":"s8t_s42","en":"Recently, zoos have been expected to play a more active role in animal species conservation.","ja":"動物園は近年，動物の種の保存においてより積極的な役割を演じるよう期待されるようになった。"},
             {"id":"s8t_s43","en":"To prevent endangered animals from becoming extinct, and to restore their populations, two methods have been adopted: on-site and off-site conservation.","ja":"絶滅の危機にある動物が死滅するのを妨げるために，そしてその個体数を回復するために，オンサイト保存とオフサイト保存という2つの方式が採用されている。"},
             {"id":"s8t_s44","en":"The former tries to preserve species through working in their natural surroundings, while the latter tries to protect and breed species in captivity and aims to return them back to the wild.","ja":"前者は自然環境の中で働くことを通じて種を保存しようとするのに対して，後者は動物園の中で種の保護と飼育を行い，再び野生に戻すことを試みる。"},
             {"id":"s8t_s45","en":"Japanese zoos have been actively involved in off-site conservation and have had positive results.","ja":"日本の動物園はオフサイト保存に積極的に参加し，成果を上げてきた。"},
             {"id":"s8t_s46","en":"Two good examples are the crested ibis (<em>toki</em>) and the white stork (<em>kounotori</em>).","ja":"2つの良い例が，トキとコウノトリである。"},
             {"id":"s8t_s47","en":"Although they once disappeared from the natural world, their numbers have been growing due to the efforts of zoos.","ja":"これらはかつて自然界から姿を消したが，動物園の努力によってその数が増えてきている。"}
        ]]},
        {"id":"source_b","title":{"en":"Source B","ja":"資料B"},
         "inline_solve_markers":[
             {"after_paragraph":0,"question_ids":["問5"],"answer_numbers":[44]}
         ],
         "paragraphs":[[
             {"id":"s8t_s48","en":"Kids like animals, but <em>which</em> animals do they like?","ja":"子どもは動物が好きだが，好きな動物はどれなのだろう。"},
             {"id":"s8t_s49","en":"Three hundred Japanese children aged three to six were shown various animals and asked whether they liked them.","ja":"3歳から6歳の日本人児童300人が，いろいろな動物を見せられ，その動物が好きかどうか問われた。"},
             {"id":"s8t_s50","en":"The number of \u201clikes\u201d for each animal was noted and the top 10 are shown in the table.","ja":"それぞれの動物の「好き」の数が記録され，上位10位が表に示されている。"},
             {"id":"s8t_s51","en":"Checked animals are those that, in Japan, can be seen only in zoos (including safari parks).","ja":"チェックが付いている動物は，日本では動物園（サファリパークも含む）でしか見られない動物である。"}
         ]],
         "table_data":{
             "headers":["Rank","Animal","Likes","Zoo"],
             "headers_ja":["順位","動物","好き","動物園"],
             "rows":[
                 [1,"cat",205,""],
                 [2,"dog",175,""],
                 [3,"panda",157,"\u2713"],
                 [4,"lion",143,"\u2713"],
                 [5,"elephant",130,"\u2713"],
                 [6,"rabbit",110,""],
                 [7,"giraffe",80,"\u2713"],
                 [8,"koala",65,"\u2713"],
                 [9,"tiger",52,"\u2713"],
                 [10,"kangaroo",38,"\u2713"]
             ]
         }}
    ]

if __name__=='__main__':
    print(json.dumps(get_passages(),ensure_ascii=False,indent=2)[:200])
    print('passages OK, count:',len(get_passages()))
