#!/usr/bin/env python
import os
os.environ["DATABRICKS_TOKEN"] = "dapi19071d5dfd98a338b5e203d6eaca857f-3"

import os
import requests
import pandas as pd

my_data = {
    "author": {0: "Jacques de Seingalt"},
    "published": {0: "2016-11-24T03:01:28.961+02:00"},
    "title": {0: "an exploration of finding meaning in life through logotherapy"},
    "text": {0: "hillary clinton waiting in wings of stage since  am for dnc speech philadelphiasaying she arrived hours before any of the members of the production crew sources confirmed thursday that presidential nominee hillary clinton has been waiting in the wings of the wells fargo center stage since six oclock this morning to deliver her speech at the democratic national convention depressed buttercovered tom vilsack enters sixth day of corn bender after losing vp spot washingtonsaying she has grown increasingly concerned about her husbands mental and physical wellbeing since last friday christie vilsack the wife of agriculture secretary tom vilsack told reporters thursday that the despondent buttercovered cabinet member has entered the sixth day of a destructive corn bender after being passed over for the democratic vice presidential spot dnc speech i am proud to say i walked in on bill and hillary having sex a friend of the clinton family describes a hillary who america never gets to see the one he saw having sex trump sick and tired of mainstream media always trying to put his words into some sort of context new yorkemphasizing that the practice was just more evidence of journalists bias against him republican presidential nominee donald trump stated thursday that he was sick and tired of the mainstream media always attempting to place his words into some kind of context whos speaking at the dnc day  here is a guide to the major speakers who will be addressing attendees on the final night of the  democratic national convention bound gagged joaquin castro horrified by what his identical twin brother might be doing out on dnc floor philadelphiastruggling to free himself from the tightly wound lengths of rope binding his wrists and ankles together bruised and gagged texas congressman joaquin castro was reportedly horrified by what his identical twin brother secretary of housing and urban development julian castro might be out doing on the floor of the dnc thursday obama hillary will fight to protect my legacy even the truly detestable parts philadelphiaemphasizing the former secretary of states competence and tenacity during his democratic national convention address wednesday night president barack obama praised hillary clinton as someone who would work tirelessly to defend and advance the legacy he had built even the truly repugnant parts tim kaine clearly tuning out in middle of boring vice presidential acceptance speech philadelphiadescribing the look of total disinterest on his face and noting how he kept peering down at his watch as the speech progressed sources at the democratic national convention said that virginia senator tim kaine clearly began tuning out partway through the boring vice presidential acceptance address wednesday night cannon overshoots tim kaine across wells fargo center philadelphianoting that the vice presidential nominee had been launched nearly  feet into the air during his entrance into the democratic national convention wednesday night sources reported that the cannon at the back of the wells fargo center had accidentally overshot tim kaine across the arena sending him crashing to the stage several dozen feet beyond the erected safety net biden regales dnc with story of s girl band vixen breaking hard rocks glass ceiling philadelphiadevoting a large portion of his speech to the pioneering stiffyinducing allfemale quartet vice president joe biden regaled the democratic national convention wednesday night with the rousing story of the metal band vixen breaking hard rocks glass ceiling in the late s"},
    "language": {0: "english"},
    "site_url": {0: "returnofkings.com"},
    "main_img_url": {0: "No Image URL"},
    "type": {0: "hate"},
    "title_without_stopwords": {0: "ugly truth six leftist heroes"},
    "text_without_stopwords": {0: "saker message current saker messages russia celebrates unity day liberation moscow polish roman papists army views november comments scotts corner scott national unity day first celebrated november commemorates popular uprising lead prince dmitry pozharsky meat merchant kuzma minin ejected alien occupying forces polish roman papists army moscow november generally end time troubles foreign interventions russia name alludes idea classes russian society willingly united preserve russian statehood demise seemed inevitable even though neither tsar patriarch guide recently episode made russian movie minin pozharsky liberation moscow triptych russian land artist yuri pantyukhin russia muscovites celebrate unity day capital river dance simferopol crimea russia putin patriarch kirill bless new monument vladimir great nov president vladimir putin unveiled new monument russias first christian leader vladimir great moscow friday opening ceremony took place meters kremlin walls coincided russian national unity day vladimir putin russian president russian holiness respected muscovites dear friends greet congratulate opening monument saint equaltoapostles prince vladimir big significant event moscow whole country russian compatriots symbolic held national unity day centre capital near walls ancient kremlin heart russia vladimir putin russian president russian strong moral support cohesion unity helped ancestors overcome difficulties live win glory fatherland strengthen power greatness generation generation today duty stand together modern threats challenges basing spiritual precepts invaluable traditions unity concord move forward ensuring continuity thousandyear history patriarch kirill moscow russia russian monument prince vladimir symbol unity peoples farther peoples historical rus currently living within borders many states monument farther may everywhere children live contradiction bad children forget father essential saker trenches emerging multipolar world first comment leave reply click get info formatting leave name field empty want post anonymous preferable choose name becomes clear said email address mandatory either website automatically checks spam please refer moderation policies details check make sure comment mistakenly marked spam takes time effort please patient comment appears thanks replies comment maximum formating examples use writingbbold textb results bold text iitalic texti results italic text also combine two formating tags example get bolditalic textememphasized textem results emphasized text strongstrong textstrong results strong text qa quote textq results quote text quotation marks added automatically citea phrase block text needs citedcite results phrase block text needs cited blockquotea heavier version quoting block textblockquote results heavier version quoting block text span several lines use possibilities appropriately meant help create follow discussions better way assist grasping content value comment quickly last leasta hrefhttplinkaddresscomname linka results name link need use special character paragraphs need anymore write like paragraphs separated live preview appears automatically start typing text area show comment look like send think confusing ignore code write like search articles"},
    "hasImage": {0: 0}
}
df = pd.DataFrame(data=my_data)


def create_tf_serving_json(data):
    return {
        "inputs": {name: data[name].tolist() for name in data.keys()}
        if isinstance(data, dict)
        else data.tolist()
    }


def score_model(dataset):
    url = "https://adb-4085387484934385.5.azuredatabricks.net/model/Best-Fake-News-3-14/1/invocations"
    headers = {"Authorization": f'Bearer {os.environ.get("DATABRICKS_TOKEN")}'}
    data_json = (
        dataset.to_dict(orient="split")
        if isinstance(dataset, pd.DataFrame)
        else create_tf_serving_json(dataset)
    )
    response = requests.request(method="POST", headers=headers, url=url, json=data_json)
    if response.status_code != 200:
        raise Exception(
            f"Request failed with status {response.status_code}, {response.text}"
        )
    return response.json()


if __name__ == "__main__":
    print(score_model(df))