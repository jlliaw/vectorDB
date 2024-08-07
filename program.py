# convert token to embedding
#from transformers import AutoModel
#

from transformers import AutoTokenizer, AutoModel
from huggingface_hub import login
login(token="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")

#tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
#huggingface token : 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
tokenizer = AutoTokenizer.from_pretrained("./taide8b")
model = AutoModel.from_pretrained("./taide8b")

sequence = "吐氣所含酒精濃度已達每公升0.25毫克以上之程度 竟仍基於酒後駕駛動力交通工具之犯意 於同日17時許至18時許間某時許 駕駛車牌號碼0000-00 號自用小客車上路 嗣於同日18時30分許（聲請書誤載為18時34分許） 許德文駕車行經屏東縣麟洛鄉中山路果菜市場（南下車道）前時 不慎與黃琇玟所騎乘之車牌號碼000-000 號普通重型機車發生碰撞（過失傷害部分未據告訴） 經警到場處理 並於同日19時16分許對許德文實施吐氣酒精濃度測試 測得其吐氣所含酒精濃度為每公升0.90毫克 而查悉上情 案經屏東縣政府警察局屏東分局報告臺灣屏東地方檢察署檢察官偵查後 聲請以簡易判決處刑 二、前揭犯罪事實 業據被告許德文於警詢及偵訊中均坦承不諱 核與證人黃琇玟於警詢時之證述大致相符 並有員警偵查報告、道路交通事故現場圖、道路交通事故調查報告表??、當事人酒精測定紀錄表、屏東縣○○○○○○○○○道路○○○○○○○○○○○號查詢汽車駕駛人結果、車輛詳細資料報表、現場照片等件在卷可稽 堪認被告上開任意性自白核與客觀事實相符 可以採信 故本案事證明確 被告犯行堪以認定 自應依法論科 三、論罪科刑?核被告所為 係犯刑法第185 條之3 第1 項第1 款之駕駛動力交通工具 吐氣所含酒精濃度達每公升0.25毫克以上之不能安全駕駛動力交通工具罪 ?被告前因不能安全駕駛致交通危險案件 經本院以108 年度交簡字第1442號判決判處有期徒刑4 月確定 並於108 年11月14日易科罰金執行完畢 有臺灣高等法院被告前案紀錄表在卷可參 被告受有期徒刑執行完畢後 5 年以內故意再犯本案有期徒刑以上之罪 屬累犯 應依刑法第47條第1 項之規定加重其刑 至於司法院釋字第775 號解釋 依解釋文及理由之意旨 係指構成累犯者 不分情節 一律加重最低本刑 於不符合刑法第59條所定要件之情形下 致生行為人所受之刑罰超過其所應負擔罪責之個案 不符罪刑相當原則、比例原則 於此範圍內 在修正前 為避免發生上述罪刑不相當之情形 法院就該個案應裁量是否加重最低本刑 依此 該解釋係指個案應量處最低法定刑、又無法適用刑法第59條在內減輕規定之情形 法院應依此解釋意旨裁量不予加重最低本刑（最高法院108 年度台上字第338 號判決意旨參照） 本案並無上開情事 自應依累犯規定加重其刑 附此敘明 ?爰審酌被告明知酒後駕車除危害自身安全外 亦將對其他用路人之生命、身體及財產造成高度危險 竟仍置大眾行車之公共安全於不顧 於飲酒後吐氣所含酒精濃度已逾法定標準值每公升0.25毫克之情形下 仍執意駕車上路 對於道路交通安全所生危害非輕 惟念其犯後尚能坦承犯行 並考量其前科紀錄（見卷附臺灣高等法院被告前案紀錄表 構成累犯部分不重複評價）、高職畢業之智識程度（見卷附個人基本資料查詢結果）、勉持之經濟狀況（見警詢筆錄受詢問人年籍資料欄）等一切情狀 量處如主文所示之刑 並諭知如易科罰金之折算標準 以資懲儆 四、依刑事訴訟法第449 條第1 項前段、第3 項、第454 條第1項 刑法第185 條之3 第1 項第1 款、第47條第1 項、第41條第1 項前段 刑法施行法第1 條之1 第1 項 逕以簡易判決處如主文所示之刑 五、如不服本判決 得自收受送達之日起10日內 向本院提起上訴狀 上訴於本院合議庭 六、本案經檢察官陳怡利、郭姿吟聲請以簡易判決處刑"

input_ids = tokenizer.encode(sequence, return_tensors="pt")
output = model(input_ids)
print(output)

                                           
''' text -> token -> id -> text '''
tokens = tokenizer.tokenize(sequence)
print(tokens)
ids = tokenizer.convert_tokens_to_ids(tokens)
print(ids)
decoded_string = tokenizer.decode(ids)
print(decoded_string)



