# Program Updater
https://github.com/Churitoring/Program_Updater/releases<br>
Download<br>
<br>
다운로드가 두개(Program_Updater_Program_Updater와, Program_Updater.)있습니다.<br>
Program_Updater_Program_Updater는 이 프로그램을 업데이트하기 위한 프로그램이고, Program_Updater은 설정하실 수 있는 프로그램입니다.<br>
Program_Updater_Program_Updater에서 This Program Updater를 켜주시면 자동적으로 Program_Updater가 다운로드됩니다.<br>
즉, 두개의 차이는 이 프로그램을 업데이트 해주는 코드를 받냐 안받냐의 차이입니다.<br>
사용하실때에 큰 차이점은 없습니다. 원하시는걸 받아주세요.

## 한국어 사용법
아직 한글만 지원되나, 파일과 폴더 이름은 영어로만 지어주시길 권장드립니다.<br>
!!! 본 프로그램과 동일한 경로에 lib 폴더가 존재하는 파일은 실행할 수 없습니다!!!<br>
당연히도 동일하지 않은(폴더 안에 폴더) 같은 경우에는 가능합니다.<br><br>
https://youtu.be/eZ3ckYCskww<br>
튜토리얼 유튜브 영상도 있습니다. (총 7분 30초)

### 1. 깃허브 계정 생성 및 리포지토리 생성 및 릴리즈하기
이건 여러 튜토리얼 많으니까 직접 찾아보시면 될 것 같습니다.<br>
릴리즈할때의 태그는 배포하실 프로그램의 버전 쓰시면 됩니다.<br>
아직까지 본 프로그램은 zip파일만 지원됩니다. 릴리즈 하실때 유의 바랍니다.

### 2. jsongen으로 management파일 만들기
Program Updater 폴더 안에 jsongen.exe가 있습니다.<br>
원래 json을 다루실 줄 아는 분들도 이거 쓰시는게 편할겁니다.<br>
대소문자를 구분하지는 않으나, 그냥 대소문자 맞춰서 써주세요.<br>
아래 서식에 맞춰 작성하신 후 저장 버튼을 누르시면 lib폴더 내부에 management.json이 생성됩니다. 특별한 일이 없으시면 저장 누르시고 끄시면 됩니다.<br>
혹시라도 확인이 필요하시면 lib 폴더 내부에 management.json이 생성되었는지 확인하시면 됩니다. 저장하지 않으시면 management.json 파일이 없으실겁니다.

#### jsongen의 기능 - GitHub Repository
해당 프로그램의 리포지토리 주소를 적으시되, 깃허브 주소는 제외하시면 됩니다.<br>
<br>
예시를 들어 본 프로그램의 주소는<br>
https://github.com/Churitoring/Program_Updater<br>
이고,<br>
jsongen에 적으실때에는 "Churitoring/Program_Updater"만 적으시면 됩니다.<br>
당연히 이대로 적으시면 안되고, 각자의 리포지토리 주소를 적어주시면 됩니다.

#### jsongen의 기능 - Executable Name
업데이트 이후 실행하실 파일의 이름을 확장자 포함해서 적으시면 됩니다.<br>
실행 파일 이름을 적으라고는 되어 있지만, 굳이 실행파일이 아니어도 됩니다. mp3파일이든 그런 다른 파일들도 정상 작동 합니다.<br>
또한, 폴더 위치에 따라 적으시면 됩니다. 만약 실행하실 파일과 본 프로그램의 위치가 동일할 경우 경로를 적으시지 않아도 됩니다.<br>
(사용하실 수 있는 최상위 폴더는 본 프로그램이 존재하는 위치이며, "\"(백슬래시)가 아닌"/"(슬래시)로 폴더를 구분합니다.)<br>
<br>
한글도 지원 됩니다.<br>
아무것도 적으시지 않으실 경우 업데이트 이후 다른 파일을 실행하지 않습니다.

#### jsongen의 기능 - Remove Folder
압축을 풀었을때의 폴더를 어떻게 하냐입니다.<br>
체크 상태면 최상위 폴더를 제외하고 압축을 풀며, 체크 해제 상태이면 최상위 폴더를 포함하고 압축을 풉니다.<br>
사람마다 압축 방식의 차이가 있어서, 이건 직접 해보시는것을 추천 드립니다.

#### jsongen의 기능 - Delete Zerobyte
체크 상태면 본 프로그램을 켰을때 본 폴더를 포함하는 이하의 폴더에서 0바이트(데이터가 존재하지 않음)파일을 삭제합니다.<br>
이 기능은 자신이 무엇을 하고 있는지 확실하게 알고 계실때에만 체크하시길 바랍니다.<br>
<br>
이 기능의 존재 이유는 다음과 같습니다.
1. 본 프로그램의 구조는 깃허브의 릴리즈의 제일 최신 파일을 다운받아서 압축을 풀고, 강제로 덮어 씌웁니다.
2. 이 구조의 이유로 파일을 삭제할 수 없습니다. 즉, 본 프로그램을 사용하실 경우 지워야 할 파일을 지울 수 없습니다. 결국, 더미데이터가 늘어납니다.
3. 그렇기 때문에, 이 기능은 필요 없는 데이터를 간접적으로 삭제하게 해주는 기능입니다.
4. 개발자가 업데이트 할때 필요 없는 데이터를 0B로 만들경우에 이 기능을 사용해주시면 해당 파일은 삭제되게 됩니다.
5. 어차피 0B로 만들면 용량 걱정 없는데 무슨 문제냐 하실 수도 있습니다. 그러실 경우 본 기능을 체크 해제 해주시면 됩니다.
6. 0B의 파일 뿐만 아니라, 빈 폴더도 같이 삭제합니다. 유의해주세요.
7. 이 기능은 이 프로그램이 들어있는 경로부터 그 아래의 모든 경로를 포함합니다. 즉, 이 프로그램이 다른 프로그램의 최상위 폴더에 존재할 경우, 다른 프로그램들의 파일도 삭제할 수 있습니다. 그러므로 (5.)에 따라서 사용을 하지 않는것을 권고 드립니다.

#### jsongen의 기능 - Delta Update
델타 업데이트를 하시려면 체크해주세요.<br>
델타 업데이트는 수정점(변경된 파일)만 업데이트 하는 방법으로, 수정점만 릴리즈 해주시면 되는 방법입니다.<br>
전체 용량은 상당하나, 개별 수정 파일의 용량은 낮을 때 사용해주시면 됩니다.<br>
당연히 이 경우 제일 첫 번째 버전은 아무것도 없는 곳 에서 수정하는 것 이므로 전체 파일을 업로드해주셔야 합니다.<br>
DoubleKiller( https://blog.naver.com/tnstn15/221039627683 )와 같은 프로그램으로 업데이트 이전 버전과 업데이트할 버전의 차이가 있는 파일만 남겨서 올려주시면 됩니다.<br>
<br>
혹시나 Delta Update 기능을 사용하다가 중단하거나, 반대의 경우에는 깃허브 리포지토리를 새로 생성해주시는것을 추천드립니다.<br>
또한, 원본 리포지토리의 management.json파일을 jsongen을 사용하여 다음과 같이 설정해주세요.(해당 리포지토리의 마지막 업데이트에 포함되게 해주세요.)
1. GitHub Repository: 변경할 리포지토리 주소
2. Executable Name, Remove Folder, Delete Zerobyte: 그대로
3. Delta Update: 반대로. 체크 되어있다면 풀고, 안되어있다면 체크해주세요.

### 3. Program Updater 커스터마이징 하기
위의 jsongen을 다 적고서 management.json 파일을 제대로 저장하였다면, 모든 파일을 복사한 이후 제대로 동작하는지 확인하기 위해 실행해주세요.<br>
복사하지 않으실 경우 제대로 작동하여 파일 양이 엄청 많아졌을때 이 파일들을 찾기 어려워서 그렇습니다.<br>
<br>
프로그램 자체의 아이콘을 변경하실때에는 resourcehacker( https://www.angusj.com/resourcehacker/ )와 같은 프로그램으로 변경해주세요.<br>
사용법( https://aboutbox.tistory.com/152 )<br>
<br>
혹은 그건 못하시겠다 하신다면 이미 만들어져 있는 본 프로그램의 바로가기 파일의 아이콘을 수정하시는 방법도 있습니다. 그럴 경우 바로가기의 이름도 원하시는 이름으로 바꾸셔야 합니다.<br>
(바로가기 파일 우클릭 → 속성 → 아이콘 변경)

### 4. 최종 적용하기
다 되셨다 하시면, Program Updater폴더 안에 있는 파일들 중 jsongen.exe를 제외한 전부를 사용하실 파일이 있는 폴더에 옮겨주세요. 옮기실 파일들은 다음과 같습니다.<br>
1. lib 폴더
2. Program Updater.exe (이름 변경 가능)
3. python311.dll
4. python3.dll (없으면 fatal error 메시지가 출력되나, 정상 작동합니다. 굳이 제외해야할 특별한 경우가 아니라면 제외하지 않는것을 추천드립니다.)
5. Program Updater.lnk (이름 변경 가능, 바로가기를 만드시지 않았다면 이 파일은 없으실겁니다. 바로가기를 안만드실거라면 이 항목은 무시하셔도 됩니다.)

혹은, 옮기시지 말고 Program Updater와 본 파일의 경로를 일치 시킨 후, Program Updater와 본 파일 총 두개를 릴리즈에 업로드 하시는 방법도 있습니다.<br>
이 방법의 경우, 매 업로드마다 두개의 파일을 업로드 해야한다는 귀찮음이 존재하나, 본 파일과 Program Updater가 섞이지 않으므로, 관리하기 편합니다.<br>
또한, 이 방법의 경우 아래에서 말 할 디스코드나 카카오톡 같은 기카 다른곳에 배포할때에도 문제 없이 배포할것만 고를 수 있습니다.<br>
하여, 옮기시지 말고 경로 일치 방법을 추천드립니다. 본 프로그램의 다운로드(릴리즈) 방식도 이 방식으로 되어있습니다. ( https://github.com/Churitoring/Program_Updater/releases )<br>

바로가기 파일이 있을 경우, 원본 Program Updater.exe 파일은 숨김 처리 하시는것이 좋습니다.<br>
또한, 자동적으로 켜지게 할("jsongen의 기능 - Executable Name"에서 지정한 파일)을 굳이 보여주고 싶지 않으시다 하셔도 숨김처리 하시면 됩니다.<br>
management.json의 경우 숨김처리 하는것을 권장합니다.<br>
(우클릭 → 속성 → 숨김(체크))<br>
<br>
Program Updater 폴더 안에 들어있는 파일들만 압축하여 배포하셔도 됩니다. 단, 이 경우에는 디스코드나 카카오톡 같은 기타 다른곳에서 배포하실때에만 사용하시고, 깃허브 릴리즈에 올리시면 안됩니다.<br>
이 때에는 숨김파일로 지정할 파일과 폴더를 미리 탑재하고, 숨김파일로 지정하셔야 합니다. 물론 내용은 중요하지 않으므로, 폴더는 빈 폴더를, 다른 파일은 아무런 내용이 없는 0B짜리 파일로 넣으셔도 됩니다.
<br>
또한, lib폴더 내부에 있는 version 파일을 지우셔야 합니다. 그렇지 않을 경우 업데이트(이 경우 최초 다운로드)가 안될수도 있습니다.<br>
<br>
릴리즈 하신 이후, 제대로 정상 작동하는지 확인해주세요.

### 5. 추가 글
엄연히 깃허브의 API를 사용하여 다운을 받는것이기 때문에, 엄청 여러번 껐다 켰다 하시면 ip 차단당하실 수 있습니다.<br>
본 프로그램은 자기 자신이 만들지 않은 릴리즈에도 사용하실 수 있습니다. 단, 위에서 말했듯, 릴리즈가 zip파일의 형태여야 합니다.<br>
<br>
본 프로그램이 만들어진 이유는 쯔꾸르(RPG MAKER) 게임을 위해 만들어졌습니다. 하지만, 범용성 있게 넓혀가고 있습니다.<br>
This Program Updater.exe는 말 그래도 본 프로그램을 업데이트 해주는 기능을 담고 있습니다. 단, 정상적으로 작동하는지 확인하지는 않았습니다.<br>
그런 이유로, Program Updater.exe를 수정하여 업데이트 하는 행위 또한 정상적으로 작동하는지 확인하지 않았기에, 해당 행위는 권장드리지 않습니다.
