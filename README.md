# py Co-Win
### "Start looking for vaccination centers the python way"

## Configs 

* `district_id` (int) - District id can be seen [here](https://github.com/PSNAppz/pycowin/blob/master/data/districts.csv)
* `show_min_18` (boolean) - Show vaccination centers for 18 and above
* `min_availability` (int) - Set min availability of vaccines

## Sample Output
<pre>
    center_id                            Name                                            address  ... Min Age Limit Available Capacity        Date
0      699611             PHC JHAJHU COVAXINE                                        Jhajjhu PHC  ...            45                  0  13-05-2021
1      609467             CHC Kolayat Covaxin                                        CHC Kolayat  ...            45                  0  13-05-2021
2      677922  UPHC MURLIDHAR COLONY COVAXINE                          MURLIDHAR VYAS COLONY BKN  ...            45                  0  13-05-2021
3      699615     CHC Sri Dungargarh COVAXINE                         CHC Sri Dungargarh Bikaner  ...            45                  0  13-05-2021
4      617804               UPHC NO 4 COVAXIN                      UPHC No 4 VIVEK NAGAR BIKANER  ...            45                  0  13-05-2021
5      677917     UPHC INDIRA COLONY COVAXINE                             UPHC INDIRA COLONY BKN  ...            45                  0  13-05-2021
6      616151        UPHC TILAK NAGAR COVAXIN                                TILAK NAGAR BIKANER  ...            45                  0  13-05-2021
7      618958    UPHC RAMPURA LALGARH COVAXIN                       UPHC RAMPURA LALGARH BIKANER  ...            45                  0  13-05-2021
8      678180  DISTRICT HOSPITAL BKN COVAXINE  DISTRICT HOSPITAL BKN COVAXINE NEAR JASSUSAR G...  ...            45                  0  13-05-2021
9      699609             PHC Dasori COVAXINE                                 PHC Dasori Kolayat  ...            45                  0  13-05-2021
10     617781             CHC Deshnok Covaxin                                CHC DESHNOK Deshnok  ...            45                  0  13-05-2021
11     544807                       CHC HADDA                                          CHC Hadda  ...            45                  0  13-05-2021
12     609573         CHC Chhatargarh Covaxin                          CHC Chhatargarh Khajuwala  ...            45                  0  13-05-2021
13     681950     UPHC SRI DUNGARGARH COVAXIN                        UPHC SRI DUNGARGARH BIKANER  ...            45                  0  13-05-2021
14     626514    UPHC SARVODAYA BASTI Covaxin                       UPHC SARVODAYA BASTI Bikaner  ...            45                  0  13-05-2021
15     677893          UPHC NO 2 COVAXINE 2.0                              BHUJIYA BAJAR BIKANER  ...            45                  0  13-05-2021
16     609580               CHC Pugal Covaxin                                          CHC Pugal  ...            45                  0  13-05-2021
17     682842              UPHC NOKHA COVAXIN                                         UPHC NOKHA  ...            45                  0  13-05-2021
18     694110           CHC DESHNOK (18 PLUS)                                        CHC DESHNOK  ...            18                  0  13-05-2021
19     609512           CHC Khajuwala Covaxin                                      CHC Khajuwala  ...            45                  0  13-05-2021
20     677903          UPHC NO 5 COVAXINE 2.0                                  ZINA ROAD BIKANER  ...            45                  0  13-05-2021
21     626305          UPHC MP COLONY COVAXIN                                  MP COLONY BIKANER  ...            45                  0  13-05-2021
22     677896          UPHC NO 3 COVAXINE 2.0                               DHANPAT RAI MARK BKN  ...            45                  0  13-05-2021
23     694380         CHC KHAJUWALA (18 PLUS)                                      CHC KHAJUWALA  ...            18                  0  13-05-2021
24     700081          PHC Kudsu 2.0 COVAXINE                                    PHC Kudsu Nokha  ...            45                  0  13-05-2021
25     618952               UPHC NO 7 COVAXIN      City Dispensary No 7 Rani Bazar Ind Area UPHC  ...            45                  0  13-05-2021
26     617785             CHC Napasar Covaxin                                        CHC Napasar  ...            45                  0  13-05-2021
27     700083          SC BILANIASAR COVAXINE                   SC BILANIASAR(PHC MAINSAR) NOKHA  ...            45                  0  13-05-2021
28     699608               PHC GODU COVAXINE                                   Godu Phc Kolayat  ...            45                  0  13-05-2021
29     694381      CHC LOONKARANSAR (18 PLUS)                                   CHC LOONKARANSAR  ...            18                  0  13-05-2021
30     677907          UPHC NO 6 COVAXINE 2.0                              NATHUSAR GATE BIKANER  ...            45                  0  13-05-2021
31     618946               UPHC NO 1 COVAXIN                      UPHC 01 Old Jail Road Bikaner  ...            45                  0  13-05-2021
</pre>


### Credits
- https://www.cowin.gov.in/home
- https://www.python.org
- https://pandas.pydata.org
- https://github.com/misalraj/vaccine_availability_info/
