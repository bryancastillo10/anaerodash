import streamlit as st
from utility.auxilliary import whitespaces
from utility.auth import user_auth_system
from lang.language import select_language

st.set_page_config(page_title="Guidelines", page_icon="📖", layout="wide")
with open("utility/style.css") as style:
    st.markdown(f"<style>{style.read()}</style>", unsafe_allow_html=True)

##User Authentication System ###
name, authentication_status, username, authenticator = user_auth_system()
if authentication_status == False:
    st.error("Username/Password is incorrect 😣")

if authentication_status == None:
    st.info(
        "Welcome to the AnaeroDash APP: An Application dedicated for Anaerobic Digestion Treatment Plant Evaluation.\
        Please login with appropriate username and password to get started.",
        icon="🌐",
    )
    st.markdown("Prototype_v_1.0 made by Bryan")

if authentication_status:
  ## Multi-Language Options
  text = select_language(page_num=2)

  st.title(f":green[{text['guidetitle']}] " + text['guidetitle2'] + ":potable_water:")

  with st.sidebar:
    st.title(text['welcome'])

    whitespaces(2)
    st.image("utility/images/biogas_plant.png", width=200)
    whitespaces(1)
    authenticator.logout(text["logout"], "sidebar")

  ## Streamlit Layout ##
  st.subheader(text['app_intro'])
  st.markdown(f"""
  <div class="grid-container">
  <h2>{text['what']}</h2>
  <p>{text['par1']}</p>
  <p>{text['par2']}</p>
  <h2>{text['who']}</h2>
  <p>{text['who_ans1']}</p>
  <p>{text['who_ans2']}</p>
  <h2>{text['how']}</h2>
  <p>{text['how_ans1']}</p>
  </div>
  """, unsafe_allow_html=True)
  st.write(f""" 
  <div>
  <table id="guideline">
      <tr>
        <th>{text['param']}</th>
        <th>{text['column_form']}</th>
        <th>{text['value_form']}</th>
        <th>{text['app_cap']}</th>
      </tr>
      <tr>
        <td>{text['date1']}</td>
        <td>Date</td>
        <td>{text['dt']}</td>
        <td>{text['app_1']}</td>
      </tr>
      <tr>
        <td>{text['app_1']}</td>
        <td>Unit</td>
        <td>{text['category']}
        <span class="unit_highlight">Influent</span>,
        <span class="unit_highlight">Acid_Tank</span> {text['and1']} 
        <span class="unit_highlight">AD</span> </td>
        <td>{text['app_1']}</td>
      </tr>
      <tr>
      <tr>
        <td>pH</td>
        <td>pH</td>
        <td>{text['integerph']} </td>
        <td>{text['app_2']}</td>
      </tr>
      <tr>
        <td>{text['temp']}</td>
        <td>Temp</td>
        <td>{text['integertemp']}</td>
        <td>{text['app_2']}</td>
      </tr>
      <tr>
          <td>{text['orp']}</td>
          <td>ORP</td>
          <td>{text['orp_value']}</td>
          <td>{text['app_2']}</td>
      </tr>
      <tr>
          <td>{text['tCOD']}</td>
          <td>CODt</td>
          <td>{text['codvalue']}</td>
          <td>{text['app_3']}</td>
        </tr>
        <tr>
          <td>{text['sCOD']}</td>
          <td>CODs</td>
          <td>{text['value_scod']}</td>
          <td>{text['app_3']}</td>
        </tr>
        <tr>
          <td>{text['tkn']}</td>
          <td>TKN</td>
          <td>{text['codvalue']}</td>
          <td>{text['app_4']}</td>
        </tr>
        <tr>
          <td>{text['nh3']}</td>
          <td>NH3</td>
          <td>{text['value_nh3']}</td>
          <td>{text['app_4']}</td>
        </tr>
        <tr>
          <td>{text['ts']}</td>
          <td>TS</td>
          <td>{text['ts_value']}</td>
          <td>{text['app_5']}</td>
        </tr>
        <tr>
          <td>{text['vs']}</td>
          <td>VS</td>
          <td>{text['vs_value']}</td>
          <td>{text['app_5']}</td>
        </tr>
        <tr>
          <td>{text['gas']}</td>
          <td>Biogas</td>
          <td>{text['codvalue']}</td>
          <td>{text['biogasplot']}</td>
        </tr>
    </table>
  </div> 
  """,unsafe_allow_html=True)
  st.write(f"""
  <br>
  <p>{text['how_ans2']}</p>
  <h2>{text['additional']}</h2>
  <p>{text['features']}</p>
  """,unsafe_allow_html=True)
