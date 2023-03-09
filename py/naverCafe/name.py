from bs4 import BeautifulSoup

html = '''
<html>
<tbody><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #00a84b;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-f09d9d80-e189-41d6-811f-8b583bf037dd"><span style="color:#ffffff;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-5cd9991e-c13d-4bca-83af-9a3bd8fa8bbe"><b>번호</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.11%; height: 31.0px; border:none; background-color: #00a84b;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-a8965391-a6b1-4f64-a615-3862d2067c93"><span style="color:#ffffff;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-94da6990-91c9-4bf5-966d-887269dd9b04"><b>공모명</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.63%; height: 31.0px; border:none; background-color: #00a84b;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-07000643-ddf9-4d8b-a4ed-7a613f9689e3"><span style="color:#ffffff;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-fc1a12bb-1306-46b4-b4ad-f5fd0b519008"><b>의미</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #ffffff;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-c4179b3c-3906-4990-8109-32bf2988788f"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-f1faeee9-3337-462b-86ee-b65254f14a66"><b>1</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #ffffff;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-f021ca54-4cad-4987-afaf-7cb2ef4e7428"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-448b0c91-3a14-49c7-91ee-d139035a0780"><b>검단 제일풍경채 2차 에듀&amp;파크</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #ffffff;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-bb94bf08-9251-47fe-97e6-17f3c60ed6f3"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-08383352-8aa6-40ad-b9b3-ef6cc5eeea6a"><b>횡단보도 앞 유/초/중/고교 학세권, 아파트 단지 뒤 황화산 근린공원 및 검단신도시, U자형 공원으로 이뤄지는 파크를 더했음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-1317ea7f-5427-4f80-8bdf-8800545dd00c"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-a1986172-a2eb-4ba8-8497-8b0822e1cdc3"><b>2</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-6c8d6a5c-45b7-43d3-8173-321953baebef"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-5bed7341-ad18-46f4-99fd-3bed6a8d428f"><b>풍경채 그랑 에듀</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-762104a6-646b-43a5-9fd3-0d53674d900b"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-0fa6e7db-acb2-43b0-a2db-0dc3737159f1"><b>쾌적한 환경 혹은 강점인 교육</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-a261dd0e-2ae2-47ba-8111-0dbc9fdf33d3"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-d5c4b8fe-2184-48ba-a6ce-2b29004b4616"><b>3</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-ef27fb14-54ed-4521-bc3e-c6aa4c8251ff"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-c46592c9-03f7-4b4c-bedd-5aa618ed17f3"><b>검단 센트럴파크펠라 (제일풍경채)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-21df41f6-dc2b-49d2-bb64-dab1b2f3feba"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-ebe5b69f-25ba-495f-be87-b6cb6e42afa1"><b>숲속의 진주, 펠라(스페인어로 진주)</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-cebb97ec-fc8f-4c21-a432-1f93778799cb"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-3bc8e9a0-dcb3-43c7-bd0d-3510e9b5dac1"><b>4</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-0be3b7cd-e295-4bbd-8a95-66c302db45f9"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-ffcadc1d-9722-4a11-b679-538850f1ddfd"><b>검단 제일풍경채 그랑포레</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-834e911e-3068-489f-b1d2-c4c74eb82f31"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-e987c302-bd2d-4fc8-9bed-5ef49a6af0fc"><b>검단 최대규모 단지와 산, 공원이 옆에 있는 맑고 쾌적한 아파트</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-7fa7026a-9bb2-411a-801b-ccf32ebc0566"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-8bb05613-7e9d-44ce-b8cd-0ba18f600263"><b>5</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-5433407c-3dad-4e8c-adf3-b892454db427"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-8c9a04e1-d45b-42b6-8a1a-7d32174ee2cc"><b>검단 제일풍경채 에듀포레</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-a2363c27-18be-4d02-a867-9d50eff38f1b"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-4f0d3a53-18b1-4faf-bdbf-07a0d3189a25"><b>에듀+포레스트의 합성어, 학세권과 숲(산, 공원)</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-0cbe96b1-4c7e-4944-92e5-2acf32ed2fd5"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-0a783a7d-fb0d-4e13-a0d2-db5970d23c46"><b>6</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-a2a7cf7b-b172-45e7-acaf-568f827b3120"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-8e385f00-9d69-421d-9f8b-d437a67cbfdd"><b>검단 제일풍경채2차 온새미로</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-6bee909a-8b17-4f4a-9a35-a0f6b9dd1e10"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-fab7bf98-a82b-409a-a138-4694d6d3d5fe"><b>자연 그대로, 언제나 변함없이</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-95cb20b4-92ed-4dff-b019-e081aa0139b0"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-7fd372ce-67b4-4a96-8ad6-fe4538f908f5"><b>7</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-fb2ba506-c71f-411a-8834-f5dfdd772b65"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-7da113e6-be8c-4427-872b-d3c31a346f31"><b>검단 제일풍경채 그랜드 노블(grand noble)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-a8c9345b-1841-4e79-a07d-f3c9d23758a3"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-8d8bff74-63ff-494f-9bbc-d07a8e5c801c"><b>거대한 상류층/검단 제일 큰 대단지의 그랜드, 검단 제일 상류층이 되길 바람</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-24acdfb1-2ba9-43bb-b377-576036415838"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-13185977-f2b4-42b7-8bd8-fbfbf394e759"><b>8</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-f19c1ccb-dd30-429d-8a47-46d1c682321c"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-1d9a0812-6f2b-4c09-badb-b8b0575a2047"><b>검단 제일풍경채 더에듀포레</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-75cd85dc-82ec-41d2-a0b8-d5a3aa8f5436"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-124ea1ac-ed82-4a70-b10c-6f44fa19d9c5"><b>학군, 숲 조성단지 강조</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-91e43ad1-6339-4af2-9da1-c040dfe99dca"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-6a1fd2cf-8e30-467f-a9e0-d0c18b8d998e"><b>9</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-1d5601f3-c525-4b5d-9a15-ff4290c3db8f"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-5e209fe9-a19c-4fce-972a-61977c1a72b7"><b>검단 제일풍경채 센트럴포레</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-7006f280-ec8b-43ff-9f47-aea8bd827dff"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-f9a8a52a-5483-46da-8ffd-8d53e40f2752"><b>검단의 중심에 있으면서 공원의 장점을 강조</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-186b8c78-40b8-4f4f-8fed-486d4ff20b59"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-97518abb-2bf5-4248-b66f-755de411698b"><b>10</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-fffca092-3a5b-4d45-aafe-00538b2f2c83"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-f50b13a0-669c-4c9b-993f-2800fa54c923"><b>풍경채 그리니티 (Greenity)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-0b115dae-e1a5-42bc-af7f-33ddef2ea083"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-0b92e639-37d8-4380-9983-fbd4c02a84b2"><b>풍경채=아름다운 풍경이 있는 집, 그린+트리니티(Green+trinity) 합성어 / 팍세권, 학세권, 역세권의 장점을 내포하는 합성어</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-dc387019-e96d-430a-ba46-cfad69713e25"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-8f515373-af5c-4416-9718-34de7347d8d3"><b>11</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-88a54595-e1fe-451d-84fb-9b268a4d00b2"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-82b23abe-77a3-40c6-a56b-9c2b60b6f423"><b>제일풍경채 센트럴파크</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-57fb6297-4d27-449c-9e41-c0ea755622c1"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-74bed075-edb0-4002-ba5b-3e20286209c7"><b>중심가를 뜻하는 형용사 Central과 자연과의 조화를 뜻하는 Park, 초/중/고를 품은 아파트이지만 에듀는 교육 쪽으로만 초점을 두는 것 같아 다른 장점을 가릴 수 있을 것 같음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-c0c1ba77-c221-43d4-a115-e080264f8956"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-a350cd78-c674-4380-8ec8-27ca649d00f8"><b>12</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-e2537d00-0555-433e-b6cd-4f356a688c68"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-298bcede-fed9-4909-91af-6c2bbc208aac"><b>제일풍경채 오투그란데</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-b08c2e29-68a1-4e8e-9d8a-81a362f1efe8"><span style="" class="se-fs-fs16 se-ff-nanummaruburi   " id="SE-152bf3f3-597d-4897-a673-13a3f1fedd5a"><b>102역 및 단지주변으로 학원가 형성으로 역세권 및 학세권이며, 단지 옆의 황화산 및 근린공원의 숲세권으로서 맑은 공기, 즉, 산소를 뜻하는 화학 원소기호 O2와, 넓다, 많다는 의미의 이태리어 그란데를 써서 '학교(학원)와 산소가 많다 것과 대단지'라는 의미가 담겨있음.</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-f4d8f11a-9452-484f-919d-c840b61180c1"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-537c1536-6801-4ddf-95c1-67e8a4eef490"><b>13</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-2e5bf224-8c8d-47b5-b0ba-ff70c150a091"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-ee878091-5655-4f70-8bcd-2fc630460812"><b>검단 제일풍경채 그랑트리니티</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-2c6c45f2-ba16-4736-ad79-293aa79afafd"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-347f04be-0b72-43f2-bdb0-07bb8cbc029b"><b>세 가지 좋은 환경(숲세권, 역세권, 학세권)을 갖춘 대단지 제일풍경채</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-b5d07c7d-c51e-4c34-a979-9f390af6b0c1"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-d1bca24a-f4f1-452d-8d0c-5fa30135f870"><b>14</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-c717371e-b5d3-4092-866d-5f5fc5d8e87b"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-317cadf4-2b2b-4aeb-a6c0-70ad83f5811e"><b>풍경채 라 그란데</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-e0d576db-2a37-44c7-a954-71c21491aae5"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-289d4fb6-dfe0-4b7a-9e94-d2fb24ff5109"><b>검단에서 제일 큰 대단지</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-b99bb98a-542b-450a-b517-75f76a80aced"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-024b3df0-4047-49b4-9b54-3d1907557972"><b>15</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-edb9c65f-ea18-4fd3-bb51-aa383e1fe813"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-32ffc990-3833-4fd2-890d-7d4e60f13d0d"><b>제일풍경채2차 그랜드파크</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-bc4a608a-bf2a-480e-8d01-a152b12ff8a8"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-9de20560-407a-4f00-888d-ff69e6b07ee3"><b>황화산 숲세권 대단지</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-e38d92e4-b89e-4d74-9876-d022bd0e0a62"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-1980e7ba-545e-4ef0-b1b2-3d0fa1814c8d"><b>16</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-a7d36f20-bacd-4f20-8633-51d84fc66a5b"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-accd0b9e-5182-406f-92c2-5aeae30d207f"><b>검단 제일풍경채 더 오메가포레</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-54c7f236-acba-432b-a51b-8f8dbd06c291"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-dbf23749-8474-497b-ac65-3037bfcf2c61"><b>검단 내 숲세권 끝판왕(Omega)의 의미를 담았음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-b2b3ea64-23b1-48fb-aa73-77d187053b60"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-04491352-82ca-4155-b1b8-03611ff75e56"><b>17</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-8b95a2bf-1a84-4945-b0dd-5ad24cf34d96"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-01b2d077-4484-4db8-b552-93f284273de7"><b>○○역 제일풍경채</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-04961d67-060e-441e-a0cc-40b0c3d0664c"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-b34e9469-f46a-456c-b9b9-48eb5878754d"><b>단지의 가장 큰 특징인 서울과 가까운 역세권이라는 점을 강조, 가까운 미래에 GTX나 5호선이 102역으로 유치된다면 이름 자체가 브랜드가 될 것으로 생각</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-97fc8bab-dacd-42e9-accb-27f535679488"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-33772b80-ce1a-46d6-a2f9-beff77713a7a"><b>18</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-f4e7d332-804f-47b8-ab63-dbe655f6e59e"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-46f755ce-b2d3-47a7-a4d7-00679762179d"><b>검단 풍경채 원베일리</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-89378f31-bd10-4bf0-aec6-acccbb93bb5b"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-e98b8999-208d-40a0-b9d8-3a74422d989a"><b>베일리는 중세시대 영주들이 살던 성의 중심부를 뜻함, 그 중 최고인 ONE을 합쳤음, 중심중의 중심, 예부터 가장 큰 건물이 중심이 됨, 검단에서 큰 단지임을 뜻함</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-d1f625dd-260a-4159-b3ac-80218949b363"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-6736b752-27cc-45e5-9865-96636f558d5f"><b>19</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-b2c39b74-3798-4696-bde6-338b7147efb5"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-ba1e1fb9-8b2f-4566-b57e-ef8698f7836d"><b>검단 풍경채 그랑디움</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-9c8736c2-9966-4957-9e4d-8189788f2e84"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-7d30e66b-d0ea-4700-9cb5-59733f4c89d9"><b>대단지 Grand, 공간이라는 뜻의 독일어 Raum을 합침, 검단 신도시 내 최고 대단지, 트리플세권(숲, 학교, 역), 대단지 커뮤니티 시설 등 모든 것이 최고라는 의미</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-351ac5ce-1a0a-4fea-a25f-8085d0efa641"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-302d0485-e802-4f2c-b41c-7bf8271abf60"><b>20</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-a44b6518-81d5-483a-97b1-abb3f14ecea6"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-90dbf78d-a728-4203-8939-e0860265ce8b"><b>검단 풍경채 헤리티지</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-a30b7e60-9bab-4625-9982-ea9822468446"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-57c2fc4c-40dc-4938-9da4-8074b94b1605"><b>아파트가 위치한 불로동의 지명 유래를 본따 오래오래 살면서 자식들에게 유산(Heritage)으로 남겨줄 수 있는 멋진 아파트가 되자는 의미</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-57b64007-1294-49d5-9875-9fc12932286b"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-e404466d-f703-4c92-8e5c-ab0c27252d55"><b>21</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-978d0f03-0656-4794-b7a7-6d2c205f98cc"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-207c2335-8213-44bc-986a-5021ef21da84"><b>the PungKyeongChae life(더 풍경채 라이프)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-39115a88-f9d9-407a-b2d0-d60fb522a2cc"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-fb66c517-ff83-4297-b2be-e610fe048607"><b>심플하게 누구나 알고 있고, 살고 싶다는 의미, 외우기 쉬움</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-a7a7e447-a194-4564-8583-505257526be9"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-8f93bc2c-0b4e-4e42-8aca-9e7866a875a0"><b>22</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-a30cc906-e5b8-4882-b6d6-56fac48ae496"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-1d4f56ce-bf49-46ff-8150-05abe43710d4"><b>제일풍경채 그란뜰 GRANDLE</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-b0a20dc7-2e06-4d0e-b30b-74cd5d334ed6"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-80ae3f97-2056-4759-88a7-eb41481c89aa"><b>큰 뜰이라는 의미</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-1f6cfdab-773d-4fa2-a66c-29b75b5a72bd"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-88fa45bb-f044-450c-b0a6-8bd3e85a92c5"><b>23</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-73ec618f-da2f-46af-9797-9212a0e971e8"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-29287a0f-5f7f-4568-bdeb-c44aab8bd320"><b>검단 제일풍경채 2차 아띠마을</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-d65fe068-d492-4496-9012-0eece5f025d0"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-c548f51e-b99d-48d3-ade2-ea483fefe3df"><b>아띠가 사랑이라는 뜻의 순 우리말</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-84e02c1e-1267-4551-997c-224664d66c70"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-236ea579-365f-4d14-bb6d-bbf98907a5df"><b>24</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-95d3f99b-29d1-4150-94f9-969769286a48"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-4714f6e5-1241-42c5-ae3b-e6f1ec5b3b5b"><b>검단 풍경채 어바니티</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-9b6abf7e-8b7a-4a5d-9121-33cbeecb558e"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-048762be-91f1-4d36-b3b0-f89d94748940"><b>완벽한 도시의, 세련된이라는 뜻, 판교 풍경채 어바니티의 고급스러움을 함께 가져가고 싶음을 담았음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-a89b348a-45d1-4bd0-8c31-ae790310c14d"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-f6b93617-3951-44b8-8429-e7b591d986ba"><b>25</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-af345ba7-2afb-42e3-a882-a606c93cd402"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-e67a658b-4949-4894-ad14-bf39a3566ace"><b>풍경채 그레이스풀 (graceful)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-d4b32d9b-cd55-417f-8440-62f9f9868912"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-43936be8-8f1d-480a-afc8-7938b00918d8"><b>우아하고 고급진 풍경채, 늘 품위를 지키는 검단의 중심이 되자는 의미</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-a5b7d69b-8e6d-4f44-8783-11488c6d9c95"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-58f095e8-235e-4a3d-a1cb-d6bf14a85e2f"><b>26</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-d3dd7236-d645-4130-bbce-796547d42c10"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-f77dc3ef-d047-4802-9090-65e2a0fead41"><b>풍경채 에르모소 (hermoso)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-71add9e1-8d08-4c3c-95bc-56e713107b89"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-e22f4948-054d-48c2-b924-f3da8e4fbe47"><b>스페인어로 아름다운, 예쁜, 고운이라는 뜻으로 한글로 4글자라 예쁠 것 같음, 문주로 만들어도 깔끔하고 고급져보일 것 같음, 보이는 디자인이 깔끔한 단어</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-ab3f738e-ff88-4526-adab-faa716a57c79"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-94e3b955-c023-4402-b0e8-7cf3322ae3e0"><b>27</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-8dffef50-0f6c-4878-a69e-761ae49065c8"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-c190d032-071d-4be4-8579-e5560be4e8a1"><b>제일풍경채 데 트라움(Ter Traum)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-101dc3fd-e2bc-4c61-9b14-a0d77b9432a8"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-dc1af2b7-a86d-4181-b613-5b821a3adbe0"><b>검단 트라움 혹은 트라움검단으로 간소화, 트라움은 독일어로 꿈, 환상과 소원을 뜻함, 풍경채에 당첨되길 꿈꾸었고 앞으로 꿈을 위해 살아갈 것이라며 우리 모두의 소원이 이루어지길 바라는 의미</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-2473aa26-491c-4c52-9f58-0ad89fb78926"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-b1c839e1-c9c6-4a07-a422-51325cff301c"><b>28</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-1c7d7661-28b5-4852-9c4d-78bfe460ac86"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-99f4fcaa-e3a2-45a5-a468-8190992e40d0"><b>검단 제일풍경채 트리플스퀘어</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-92c5c309-fa4b-47aa-84b2-36b596863877"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-d847f5dd-e51c-4377-ba06-c043f7852188"><b>학세권, 숲세권, 역세권 3가지 장점들이 한 곳에 모여있는 아파트</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-48eddc3e-bbeb-4063-8679-831155087231"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-5c7434e4-7a59-43a1-a7e3-91619e1f2c94"><b>29</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-44ed5be9-a7b5-4037-8fa6-948525a438ed"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-59c38854-c95f-4736-b015-2fb6bb31fe82"><b>검단 풍경채 더 트리니티 (The Trinity)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-46b7b7ff-08c5-46a3-86fa-395263a08d94"><span style="color:#333333;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-e392f39a-0478-43d1-988b-d9c44fb65b6a"><b>‘학세권, 숲세권, 역세권’ 삼위일체된 살기 좋은 단지라는 의미. 판교 풍경채 어바니티와 유사한 발음의 단어를 차용한 고급화 전략.</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-b2c82a67-3738-499e-95aa-5240fc20a273"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-692e7c59-0c03-4f29-8db0-85a54a736f19"><b>30</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-c6960efb-82b3-447c-a4d4-37ef1d75df6d"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-f9902580-ed79-40f2-a89d-d1583c2753b3"><b>제일풍경채 엘리니티</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-622ad492-2ccf-4db4-bbfa-5fe6f047bd4e"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-f3d4cca8-f28b-4050-9948-7c587d3205a5"><b>최고의 품위와 무한한 가능성이 있는 분들이 모여산다는 의미, Elite+Dignity+Infinity+Community</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-41759bea-2aef-46eb-abe9-55a3c222a8a3"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-56341fa2-2e40-4bdd-87ae-613c34bdff08"><b>31</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-cd7baca4-ce3b-47b8-b4bc-0268d2f7435b"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-6e158aa5-523c-451f-9de1-dc1f2a6cbe6d"><b>풍경채 클로리스 (Chloris)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-771fd894-9309-4f45-8093-da5d9495af6a"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-5e60ab9c-1dcc-46a8-9a52-dc175f531ae8"><b>그리스 신화의 꽃과 봄의 여신, 클로리스는 그리스어로 노란빛이 도는 녹색을 의미</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-89dea38a-b815-4df0-9a4c-4356d5550bbb"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-9aecba86-57b7-4eff-8f4b-edcfe9d49741"><b>32</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-d7111cc9-2e81-4c01-ba6e-88ff39097737"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-9c573791-9e2b-4de1-aaee-d018a06e46c7"><b>제일풍경채 더 레인보우스퀘어</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-9c688623-6bb1-4cea-9271-cf169edc396b"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-9f7d1bbc-bac7-4d47-bf22-6a698aed1dca"><b>행복 가득 다채롭고 아름답게 빛나라는 의미로 조합</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-02131870-de62-4952-8691-47da68a4f30b"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-0f474089-21ed-4f5b-a169-1c7daae6bb07"><b>33</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-f8df4ee7-91b6-4c4c-8363-481804b18500"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-bdc74d14-d0d0-4ed2-8856-18a962b35b07"><b>Pung Kyeong Chae The Grand (풍경채 더 그랜드)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-ea6cc4f5-0bcb-41ea-9d61-75d17549e898"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-23d25449-a142-4665-91ca-963e5153efc4"><b>대규모 단지</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-47c5f878-74fe-46da-ac83-35337fb5c6c7"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-0bb40aa0-44b5-4035-b4e3-002f75897d43"><b>34</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-b0e7b6b7-b50b-4c71-be91-ed4bb7a034fd"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-5da2e5c5-a991-410b-9a18-925c591f6f9f"><b>검단 풍경채 그린시티</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-c5045bc2-ef39-4a35-8321-89d77c565455"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-2533b4d3-4d4c-4cbd-bdbb-39826002cfff"><b>1700세대 큰 단지가 녹색 푸르름으로 가득 찬 뒷동산이 있고 주변에 녹지 조성이 잘 되어 있어 대단지 느낌도 살려 그린과 시티를 합쳤음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-7310a520-8251-43f0-bf60-16ddf30df956"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-ed992709-9aa2-4279-bf08-df041fb1f88f"><b>35</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-48f247a3-2e0a-4e26-b2c2-f34935bd3f5b"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-898d7af9-27db-4fec-b5f0-d8e987413814"><b>더 풍경채 웜빌리지(warm village)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-70c2b602-e087-4570-b6e1-b01a5b0d1ee9"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-ee8b42a4-8fee-4bcd-9e03-589ed6bc1081"><b>삭막한 세상에 누구나 마음이 따뜻해지는, 어느 가정이나 따뜻하고 포근한 그런 마을 혹은 공동체였으면 하는 바람을 담았음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-19ad3085-7ba8-4760-9836-343ce3b1640f"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-7fdd8dd3-fe4f-45a0-954d-39a2c1259b4e"><b>36</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-3704fd1f-5bda-4b15-b257-329a2021b892"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-73da16a7-12ee-43f6-9358-e140a2569f1b"><b>검단 월드클래스 풍경채 2</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-b7b41d61-76ea-475a-af03-1c563db88e97"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-5c815ebb-4c3c-4290-b1bb-e0bcf11141f4"><b>　</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-f3a754d9-fb7b-4145-81cd-1e4b25e127f3"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-31666e66-7e76-4012-a0d5-7c3cf730630e"><b>37</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-c5016091-58f1-4409-bd78-7e0c5777e0c5"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-186e790c-5321-461b-bb81-cb3fcfa3971c"><b>풍경채2차 퍼스티지</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-4c1f71d2-1bc1-48d8-a51d-6d3264aa4503"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-0c6356bb-89ed-4b10-a602-0155b4f4c3b3"><b>가장 앞서길 희망하는 의미</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-6696eadd-82e1-4d8e-bc19-aeabf51eb1cb"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-35b6716b-e983-4586-b1be-b81cf20a5fb6"><b>38</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-e0e61c26-99fd-45d6-80dd-b3d2a0d9eb3f"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-a8fcaa16-199e-4570-adb8-75a5765d8967"><b>검단 제일풍경채 더 그랜드</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-2e6d7072-5628-4cc6-afd7-2607c67c9a85"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-c59d6cef-f9b8-48f6-8b37-d4793eabf2a5"><b>검단신도시 가장 많은 세대수를 보유하고 있는 제일풍경채 2차의 특성을 담았음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-9df72f41-5a5d-4337-a0a2-08b4e9bd2966"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-4f416cbf-8c7d-4091-9aa7-9e942bd20523"><b>39</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-d060269e-01ef-4d94-88f8-67f09391eed7"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-61022630-8672-43bb-9799-71426af237df"><b>검단의 두번째 풍경채 더그랜드</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-e973031d-a89c-456f-a94c-fbbe2a8c9455"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-df661861-e2c8-4cd4-82aa-b34640af7461"><b>대단지를 의미, 2차 단지 표기의 수요가 있는 것 같아 포함</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-a8c86b50-c0ad-4a5b-956d-207c5c3fcb98"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-531804ea-dbd1-440a-82e7-f0550f5a94f2"><b>40</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-79995b45-3663-4112-a93b-f0c107438235"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-724d26d2-963f-41f5-9fac-ad537080645f"><b>검단 제일풍경채2차 트리플에듀</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-b2584158-957d-4bf5-b5c1-76b4d9f6cae7"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-5acce066-f233-4220-86a8-29bc8bdc358c"><b>아파트 장점 중 하나인 초/중/고 학세권을 강조할 수 있음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-c7d883e3-b24b-4d60-ac45-3b0ac7843005"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-cef298d6-8434-470b-a220-54c8eeda9b97"><b>41</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-7830656d-dc6f-4799-8adf-e18b8d915d6f"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-c924ffb6-da2b-434d-911b-6ea375289a6e"><b>검단 제일풍경채 2차 에듀포레</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-ce7f10e6-1bba-47b5-b538-8d06022505cc"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-6c039670-42d1-459b-9589-ec17b2129b75"><b>초중고에 산, 근린공원을 강조</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-343d73ae-13ca-49d3-9a27-79506ee2bfc6"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-12e8fb79-db2a-4e58-9fe8-21bf051074c1"><b>42</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-c49bae84-3a0e-4307-b268-46bcf60d66fa"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-36d33d5d-3ea8-40c9-81e2-4aee3b8e11f6"><b>제일풍경채 로얄트리플에듀</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-63e206a0-3463-42e6-a4ab-3b6dbae5e5b2"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-af6de162-bb25-47d7-bf54-dfc85ecaf9dc"><b>지하철 3개 상가지역이 유흥시설업 제한지역이니 자연적으로 학원가 형성이 될 예정이라 지리적 가치를 담아보았음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-44705a75-6916-45f1-9835-4c0a01f6a481"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-17ab0e83-9919-41e0-8851-a387d2654abd"><b>43</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-6b771eb8-38f9-40df-8de7-43e3e44ae083"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-b85d9e3e-e522-4dfb-9dce-c3ec849b9647"><b>제일 좋은 풍경채 2차</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-0ecbca82-576d-40c6-a897-ab3d9935fdaa"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-6b8d49d4-545b-4c0c-83cd-9eca7293f140"><b>뒤에 산과 공원을 두고 앞에 학교를 둔 검단에서 제일 좋은 아파트라는 의미</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-aa524f5c-aa1d-42b1-9a5c-6e809445abd0"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-852377d4-2e08-4ae5-9cc0-03f83266ec17"><b>44</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-b78655ec-f6a2-4644-a1b4-08df83a85dba"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-c8f90c86-3faa-4afc-bc6b-870f9edc8ca8"><b>검단 제일풍경채2 프리미아(Premia)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-f8f650bb-0bf6-4751-b85d-9a2fb6ecb4aa"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-a9859018-e00c-477a-95e3-35156ceb0299"><b>프리미아는 폴란드어로 보너스라는 의미, 우리 아파트는 공원/학교/지하철을 모두 포함하고 있는 삶의 보너스가 되는 의미를 담고 있음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-0303a394-29e8-4db4-9893-9b87de4bd6af"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-3e6a0d2d-df0a-4d4b-af2b-011a68725525"><b>45</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-cced8d47-0370-462a-9d8d-d052dbb773c1"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-a15024fa-d1dc-4155-852f-5f43763b39db"><b>제일풍경채 라온제나</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-4ab93400-2fa5-4fd7-a99e-4dfff99c16cd"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-aa54aa9a-4d9f-4019-b85f-003b8f030b03"><b>라온제나는 순 우리말로 즐거운 나라는 뜻, 모두 즐거운 삶을 살 수 있는 아파트가 되길 바라는 바램을 담았음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-0835a00c-55dd-4de2-96f8-410a8641e074"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-e36c4c00-02fc-4992-b452-afce60cae782"><b>46</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-dc0ce31b-d734-4d04-a01d-497f58a20bdc"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-7f4d1008-03a8-4c42-9b4f-c12c1378d58f"><b>제일 풍경채 더 포레스트</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-2008a1e7-fa5f-48c2-9032-b4de9d2416ec"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-2b0f36fb-43b4-4ed5-99f2-c13fb7e5dc93"><b>우리 아파트 최대 장점인 숲을 강조</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-fcd8103e-33b2-4940-a078-8a6f240ae644"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-8cbc3271-ae84-487a-bb61-071651f9b0e0"><b>47</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-4c421f2a-b6f7-49c9-9b19-7595e29525ff"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-17fc88d3-ea2c-448c-821b-f1fb314e2058"><b>풍경채 더 숨 [THE S'oom]</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-cb586fe6-5071-4283-856a-cf1b86858a23"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-8f6cb189-c805-4bc1-a6d6-c7ff5bd85a5f"><b>검단은 검붉은 갯벌을 뜻함, 갯벌은 숨쉬는 자연</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-e3d6ab7f-ae5c-467b-95bd-239d940b6ad2"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-5988dda5-a5e8-41b5-aaa8-3c632dc052ed"><b>48</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-9aa500f9-6652-4558-8939-833a9f1ba15b"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-70517aba-5396-4508-b9c0-e897b131c18f"><b>제일풍경채 그랜드 포레</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-00007d19-1f23-4b4e-9277-7c5217a53fea"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-e7b8f4e1-78ef-4490-8dc3-57aa46599014"><b>단지가 제일 크고 사람도 많고 옆에 산이 있음을 의미</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-2c5fc4e0-5d4b-44a3-b4c7-3cbedd7e8155"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-8dcda147-2794-4c7e-8c77-9d69ead894f5"><b>49</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-a6a26522-4320-484d-9b84-8a548051777c"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-07235121-b1f0-43b7-8b0e-c800dc34d05a"><b>검단 제일풍경채2차 트리플에듀파크</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-b5729f8d-2701-4871-be81-31a24fc39860"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-396a2a3c-4719-4cb0-8dbe-c2d80010675e"><b>학세권, 팍세권을 모두 충족하는 아파트라는 의미</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-2aa25943-02ca-4d88-9695-b6af71498118"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-46ef7b10-fbd8-47bf-96be-eab9aceb4c5f"><b>50</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-74b0c476-639d-4244-a1ad-f057eafaa537"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-2d239905-b0c1-4a92-8c7c-f5647a1b0482"><b>제일풍경채 트리플에듀</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-2a13ef2c-34e2-414f-99c3-e9b25952ba7f"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-4cf4c3f0-6203-46f2-981e-992a0fa51873"><b>　</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-01357280-9a04-4e58-80d3-c1bf99dcae03"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-5ff55fd3-194f-4396-97a2-c7a077a2f9ca"><b>51</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-626e0613-065f-4d66-88fa-b9c0704abd8e"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-c21ed936-252e-4721-a112-d2144c3d2ee6"><b>제일풍경채 걸작</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-ecf30a96-c981-44cb-9daf-ae2590c52357"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-35f91446-249a-4ae0-b7e1-89bdd5007573"><b>매우 뛰어난 작품, 훌륭한 우리 아파트가 되길 바라는 마음을 담았음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-137c14f2-6ba7-4c74-b4e2-3c18a6619607"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-5a6f72a4-115b-481c-8444-a7fe42819dd3"><b>52</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-cf5b715e-14e5-4ffb-b9fa-72f4e4af32d3"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-2f242caa-845a-4b3e-b1a4-c273dfe7606d"><b>제일 풍경채 그린나래</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-6a3ee7dd-f627-4998-9750-c1f4b50df2b0"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-065bb055-6b62-4d6c-8133-2a1b2e627f12"><b>그린나래는 순 우리말로 아름다운 날개를 뜻함, 날개는 비상을 뜻하니 가치가 돋보이는 아파트 이미지로 괜찮을 것 같음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-4a2f6f1e-b119-43b6-a6d5-580ba9060191"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-a14377fa-18d4-4de6-85e7-41b12f32010e"><b>53</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-58deb46c-1434-4b93-9563-9dce19ff7c67"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-8228def5-dd61-4931-a8a4-b59b5e32d9f3"><b>검단 풍경채 로</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-310db013-7da9-4878-b668-a1aab351b3b8"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-9a5246ff-854e-4477-bcd7-6c92276aace2"><b>한자 '길 로' 자를 뜻하며, 모든 것(학교, 공원, 사람 등)은 풍경채로 통한다는 의미</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-4c9cce21-1da0-4815-9710-6f89e8f69efb"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-d69d031e-2e8d-4c2f-9a41-7761cc68cae7"><b>54</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-13340d45-7072-4c3f-a8f4-13b8183b3294"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-dcaca928-1d94-427e-85a4-1c5b6e1a5e77"><b>검단 제일 풍경채 2차 다온</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-c909affb-97ec-4ec0-b345-4c36d45012e5"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-8e1a5adf-0d5d-4320-af3e-0fe5f7d405a7"><b>온새미로는 자연 그대로, 다온은 좋은 모든 일들이 다 오는 이라는 뜻을 가진 순 우리말</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-864ebf01-eb77-406e-bec7-7730a9fa2651"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-b94320dd-3f29-44c0-876e-40f4c56c4791"><b>55</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-ca53a5c8-5b39-48f0-bd7d-58bde041931d"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-0a8ccbe3-16d9-4529-a6bc-07bfc86e4157"><b>제일풍경채 엘리시움</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-fa323a03-9d95-4802-9507-c1b834d4f9c0"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-fb2467af-fd9e-44b4-85eb-a146253c9be1"><b>지상의 행복으로 제일풍경채에 사는 사람들이 모두 행복하길 바라는 바램을 담았음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-f25bdbcc-91b3-41c7-a5bf-ca48503adc0b"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-6c642dd3-7720-425d-9a76-4ce5ee1a2a36"><b>56</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-b86d8075-84a2-4a73-98f8-7dc640f4e21a"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-cb0ed3af-d299-426d-b10b-283bc37ec80c"><b>검단 제일풍경채 가온누리</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-d67257ce-1eaf-4856-ac49-2f2e97f36a5e"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-3c82a052-ae77-4402-b365-631a16734a3e"><b>가온누리는 세상의 중심이라는 뜻의 순 우리말</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-730ca31e-a338-4873-a228-2e191a1e70a1"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-87f98c3c-9475-4b79-82c4-543e979941c0"><b>57</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-905cd188-ae5d-4640-bd1e-9ef12881fb25"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-559ff802-6737-4cb0-a1ee-fdea1daa0f09"><b>제일 풍경채 더 숲</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-649a4c8e-a034-476a-9fa9-d1d853737bfd"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-0acaf697-3d10-4440-a93a-ccb4e5909af1"><b>숲이 가깝다는 장점을 심플하게 나타내보았음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-3238fceb-d5c0-4417-b58e-1b0e1088576c"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-05675824-6b95-4381-abe6-7fe0f0036d85"><b>58</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-4ca5c33a-8101-495b-870e-4c541e00645f"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-8a16366e-fd29-4d25-88fe-079a0ceae53b"><b>검단 제일풍경채 그랜드1734</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-786c4af7-7f04-47d6-8886-d146ac14e789"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-741edecb-b338-4e71-9363-b0335b74a9ff"><b>타 아파트와 비교했을 때 가장 큰 장점이 세대 수인 듯 하여 대단지를 강조한 그랜드와 세대 수인 1734를 합쳤음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-e21fd72a-261c-4007-85bf-6480fb17cbc7"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-dc786fc5-3634-45d9-aacc-ce54742811bc"><b>59</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-a6b548bb-9dd6-4c70-b635-11ae872a4ce1"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-86115992-5ae3-4b6a-a7f5-3b55922fa8f4"><b>검단 제일풍경채 에듀&amp;포레</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-2e596cae-3d72-4f95-ac93-ef2e7259900c"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-7c42e35c-e04c-4d0b-9bc2-2ec1a1bfe8d5"><b>학세권, 숲세권을 직설적인 단어로 표현</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-31927e6b-974c-4cd2-a731-1acbf7295331"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-aacbafa6-eb45-4189-926e-c0d6fe43c996"><b>60</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-9de5fcd8-4fc2-40eb-9995-5ee866785db3"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-a5e3d6a2-4ff9-4d6a-92e4-bb561e9fc262"><b>검단 제일풍경채 더 프라임</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-76364c3b-27d0-4882-821c-b28b65b03cf8"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-c5e8e445-2453-4cbe-bd73-c595a26c8fe8"><b>　</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-0bda5fde-05e0-469b-b459-a3fbed868367"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-ce8d9ab3-bc64-4269-827a-f304784954c7"><b>61</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-f97ea373-d76b-4205-9d89-b7692085230e"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-0517fe3e-3b33-4095-93d7-46bc7b3e0c38"><b>검단제일풍경채더베스트</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-ccddbe51-0966-45a3-acc9-c2c42cb3a586"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-7f0ccbac-01c0-4078-a28e-270ecfa530bd"><b>제일건설이고, 제일 좋은 아파트, 타 아파트에 비해 더 좋고 제일 좋다는 이미지를 담았음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-a04b8452-e5bc-4e7f-8a10-d38013095659"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-1092bc0d-d4c6-4206-83a2-5ca2bf6b5e93"><b>62</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-e12cb30a-2d6b-4fbc-9741-935134a5d119"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-d9b06342-fd6f-4b88-a0ff-be68936aad05"><b>검단 (제일)풍경채 II 빅라이프</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-e14c351a-f86d-4287-be24-1e3efc74e47b"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-13cba6aa-059e-4f04-8e23-a25f8aecca53"><b>2등, 두번째라는 아라비아 숫자 2 대신 큰 숫자의 의미로 로마자 II로 표현, 분양 시 내세운 슬로건 빅라이프가 우리 단지에 가장 잘 어울리고 함축적으로 표현하고 있다고 생각함</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-bc8c6c99-c749-4bb9-8d36-02c06dbbcc2e"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-269cbf5e-8c91-42fa-83b4-b317d8dd2b2e"><b>63</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-6c74353c-f706-471c-8af7-6d41e41f6867"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-ad42dbfe-39c1-4482-82fa-da3959fba59e"><b>검단 풍경채 그래비티 [Gravity]</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-832e6fd0-76a3-40e3-9799-00fd063c9eab"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-76554ba6-de85-4261-9e09-025f207d0ce7"><b>우리 삶의 중대한 빅라이프의 시작, 교통/교육/녹지 무엇 하나 빼놓을 수 없는 웅장하고 엄숙한 대단지 아파트, 마음을 끌어당기는 절대적인 힘을 상징</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-721f7856-0831-4652-a7f5-f893d2e703c5"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-93c81eb5-03af-4bd5-b3e8-7e47d6971e06"><b>64</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-de240e37-091b-409e-820b-ed9284431cab"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-f368571e-242f-4a9f-8bf0-be80caa0fad0"><b>풍경채 두리</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-39fe42e5-bd2c-41bc-b660-ce147fd6d191"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-a94e8f60-da10-4894-b5fa-1379df66d523"><b>둘째라는 의미로 2차를 표현, 두리는 하나로 뭉치게 되는 중심의 둘레라는 뜻의 순 우리말, 검단신도시의 중심을 뜻하고자 하고 '둘이'라는 타인들과 함께 한다는 느낌의 표현을 더함</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-b7e3fcc4-6e07-40df-92c8-20b1f0afc00f"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-c2465863-619f-4e22-8e59-dd2ab316b68c"><b>65</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-186344a3-fbb2-438b-8d74-f9dcae808a67"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-cbf2a290-fd06-4f46-b46b-2b78865bd52a"><b>검단 제일풍경채 G1</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-7b8667cb-4a6c-469e-b8d1-ddff06d89707"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-d30ac2d2-9470-45ed-920c-4b43db7275d1"><b>Great One을 뜻함</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-3c9005fe-a263-4527-9c81-2ee4e3a342b6"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-2bd515d9-0483-4d96-b28c-65eac62e3558"><b>66</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-9800fd6e-0518-4efe-95b7-4f5667aed1d2"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-c591d2d5-2719-4ddd-b38f-cd0a7109addf"><b>풍경채:움</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-59c0f87a-ca37-484f-953c-d0d27ffca545"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-959339b6-5dbb-46e6-b74f-f53fbcdb3585"><b>채움은 가득 채우다는 뜻으로 모든 것이 풍족하게 가득 채운 공간, ium(움)은 공간이라는 뜻으로 이중적인 의미가 담겨있음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-81dddb53-4a02-4502-8400-937e8c3be793"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-90ef5599-0a06-4c88-9916-4cbe610413e1"><b>67</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-8eecdaf5-e1f2-4f3c-b2a7-64d46d664409"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-39722586-545b-47e9-aa95-4c839ac20261"><b>제일풍경채 더올림 (The Ollim)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-e70358b7-e5a9-4f94-98fb-8f046da37971"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-35f7ed61-2920-44db-9bcf-48e2eab2e2ca"><b>인생, 가치, 아파트 품격, 교육, 삶의 질을 어느 아파트보다도 더 올림이라는 의미</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-8b22be82-5b20-420f-b304-dcee858e75a5"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-7dc663b6-4433-48b2-98db-89aad98e94eb"><b>68</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-de2575e5-605f-4d42-bfe3-bd2e682d818b"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-9d9742ff-fe50-4688-8e71-4fc217558db9"><b>검단 유포리아 풍경채</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-beba6a92-52d7-421a-9886-05a8e82acbe2"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-04672f0b-1b60-4523-bce5-68b3f9932057"><b>가슴 벅찬, 행복한, 희열이라는 뜻, 청약당첨의 가슴 벅찬 마음과 앞으로 풍경채에서 보낼 행복한 하루하루, 트리플세권에서의 생활을 통해 희열을 느끼며 건강하게 성장하기를 소망하는 의미</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-5ebd7a27-fc0e-4017-a309-d1217a96e7ea"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-a546f67e-f2e3-4a6a-a4b9-7e0725aa2583"><b>69</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-1eecfd92-9b67-4f91-b898-ab786f21ec16"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-6b3fb876-2457-47ce-995d-da2075b7abcf"><b>검단 늘(Neul) 풍경채</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-3276a43f-5519-43d5-89fb-1c8e5d5eb406"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-404e3f6a-4ce8-48b4-9e40-880fe7c03956"><b>언제나라는 뜻으로 '늘'이라는 단어 뒤에 붙는 문장들은 모두 긍정을 의미함</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-b18a5d3a-8198-4467-932f-f6711edb1595"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-fba49784-d3b1-4fc3-9efc-b04789815e8a"><b>70</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-6224e59f-e7a6-4dea-8b39-a19941b16c8c"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-ce9cdad0-1501-4bd8-af63-5f64a62e788c"><b>검단 풍경채 그리너스(GREEN-US)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-527bfe91-00c8-4bf5-8d76-2dc044ffdd1d"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-09728e18-329f-4641-85b1-f81a16cbc11f"><b>풍경채를 뒷받칠만한 원초적이고 간결한 의미의 Green, 입주민과 우리 모두를 뜻하는 US를 합쳤음, 아직 그리너스라는 펫네임을 사용하는 아파트가 없어서 우리가 사용할 경우 최초가 될 수 있음</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-62004685-eca6-4217-9604-04e5d72b8c21"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-84dcd5ca-41a6-426f-9fbb-aa5fe6412b5b"><b>71</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-2a544df0-7606-485e-a99f-6343dc5ec316"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-25d581ad-814f-4d9f-8047-738baaea79d9"><b>검단 풍경채 팰리스카운티(PALACE COUNTY)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-c6cdb907-cdaa-44e8-91d6-e8c25ecaaf60"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-f5e67ffc-3139-469f-9a5a-0b5920b39c8b"><b>궁전같은 집이 모여있는 주를 뜻함, 풍경이 있는 궁전같은 대단지</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-89879127-e572-4bd8-8a0f-43960116f75b"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-300c6a8c-bc0c-40ca-b0c9-ef5a99f4abfd"><b>72</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-6476ef02-1fd6-4b51-9c1b-f92d409305c5"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-7c1c76b9-6669-48cb-b862-9be329407d67"><b>풍경채 1734</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-82d5eb83-85d2-4022-a031-f98aa202d744"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-89e14698-6142-4ae8-9d1e-336f401202f4"><b>1734세대의 풍경채를 의미</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-d11bd87d-7e8e-4777-870d-5608cee06f92"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-f8f8adc9-2ae7-4df7-afd8-5e2574d9a12f"><b>73</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-72dae475-8b71-4030-87d7-94c9d02da286"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-5ba6bc82-3367-4e2d-8720-21ec19d4636f"><b>숲속의 풍경채</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-cb94d9e8-a5b9-4eb8-9ce9-76f3e81b086b"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-1f7c7fd5-ce6c-4006-bb24-6073458d82ce"><b>공원과 동산이 둘러쌓여있음을 의미, 풍경채라는 회사 네임을 필수로 가져가야 할 경우 이국적인 펫네임과 풍경채는 조화롭지 못함</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-712a1129-2380-4105-b236-2fd4cd42bc22"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-9379cadd-d838-4161-8fa9-b90d0b719ae7"><b>74</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-5954fca0-2d46-40d7-9baf-7bd7f7d8eb7c"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-b29881a1-ff21-4f77-a6a8-a59732157af7"><b>검단 풍경채 (더) 클래식</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-263f4cdb-637d-4f0a-b8bc-45eb490915ae"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-0788d0ea-02d3-45a4-ad9a-7f1e2eca7e78"><b>풍경채 자체가 자연친화적인 의미라 별도의 단어는 생략, 세월이 흘러도 격조와 품격을 유지한다는 느낌, 클래식한 아파트를 의미</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-188a22af-b6f2-42fe-8296-885fc8d4968e"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-a5cee6df-35a9-41e4-9e4b-5ac44fff8677"><b>75</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-80f90e64-1557-4e29-8d6a-2fc70bfdc2af"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-642c2465-fcf6-43d9-8925-62ed6b2caac8"><b>제일풍경채 더 그랜드</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-0f34635a-fbf2-4ba7-9883-3fa144552812"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-fdc9ac27-1a78-47d5-8e60-06949767b3e1"><b>검단에서 세대 수가 가장 많다는 점을 뜻함</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-229319a2-8278-4adc-ace4-c274e7036336"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-6f86ce27-5737-40f8-9660-50a3c3f2a8b4"><b>76</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-d1bff7c7-4bba-4862-8d4c-a0f708f1d203"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-f77ef356-eb8c-4285-ac85-4a563845864f"><b>풍경채 더 MQV(엠큐브이)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; background-color: #e2e2e2;">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-b72e551a-e1d2-4ea8-bb82-2bcd56a9e39c"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-3c12be8c-f582-496f-895c-b47810ab5351"><b>더 나은 삶의 질을 뜻하는 프랑스어들을 합성하여 표현, meilleure(더 나은, 더 좋은 등) qualite(특성, 장점, 품질 등) de vie(생명, 목숨 등)</b></span></p></div>
                
                                    </td></tr><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 8.26%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-ac324331-b846-44cf-8dd0-77c895a8db36"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-54810d29-5a76-4437-8d5b-6f2bf8859384"><b>77</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 44.06%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-center " style="" id="SE-f4fc7be3-4cc1-4b4f-82a5-4f96b5bd9f1d"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-63029fac-6fc3-49e1-816b-9c6690c4bdda"><b>풍경채 커넥션(connection)</b></span></p></div>
                
                                    </td><td class="se-cell" colspan="1" rowspan="1" style="width: 47.67%; height: 31.0px; border:none; ">
                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align-left " style="" id="SE-7f234c71-8dfb-4b89-bcc9-81671f0df9ae"><span style="color:#000000;" class="se-fs- se-ff-nanummaruburi  se-style-unset " id="SE-a338133e-cc73-4f92-a2dc-e8e397babf10"><b>5차까지 있는 풍경채를 이어주고, 1차부터 3차까지 신도시를 이어준다는 것을 의미</b></span></p></div>
                
                                    </td></tr></tbody>
</html>
'''

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the element with the id 'SE-08383352-8aa6-40ad-b9b3-ef6cc5eeea6a'
elements = soup.find_all('span')

key = 1
num = []
name = []
sub = []


# Check if element exists
if elements is not None:
    # Print the text
    for element in elements:
        print(key)
        if key == 1:
            num.append(element.get_text())
            key += 1
        elif key == 2:
            name.append(element.get_text())
            key += 1
        elif key == 3:
            sub.append(element.get_text())
            key = 1
        else:
            print("Default case")
else:
    print("Element not found.")

print(num)
print("--------------------------------------------")
print(name)
print("--------------------------------------------")
print(sub)
