# homepage.py
import streamlit as st
import base64


def app():

    #st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")[image]

    # uploaded_file = st.file_uploader("safety.jpg", type="jpg")
    #
    # if uploaded_file is not None:
    #     # Convert the file to an opencv image.
    #     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    #     opencv_image = cv2.imdecode(file_bytes, 1)
    #
    #     # Now do something with the image! For example, let's display it:
    #     st.image(opencv_image, channels="BGR")

    @st.cache(allow_output_mutation=True)
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    # def set_png_as_page_bg(png_file):
    #     bin_str = get_base64_of_bin_file(png_file)
    #     page_bg_img = '''
    #     <style>
    #     body {
    #     background-image: url("data:image/png;base64,%s");
    #     background-size: cover;
    #     }
    #     </style>
    #     ''' % bin_str
    #
    #     st.markdown(page_bg_img, unsafe_allow_html=True)
    #     return
    #
    # set_png_as_page_bg('imag1.png')

    main_bg = "back.png"
    main_bg_ext = "back.png"

    side_bg = "back.png"
    side_bg_ext = "back.png"

    st.markdown(
        f"""

       
        <style>
        .reportview-container {{
            background: #E55D87;  /* fallback for old browsers */
background: -webkit-linear-gradient(to right, #5FC3E4, #E55D87);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #5FC3E4, #E55D87); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

        }}
       
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
        <style>
        .sidebar .sidebar-content {

        color: #35b7aa;
        background-color: #35b7aa;
    }
        </style>
            """, unsafe_allow_html=True)

    # st.title('ABOUT OUR SOFTWARE ')
    st.markdown("<h1 style='text-align: center; color: #7b113a;'>ABOUT US</h1>",
                unsafe_allow_html=True)
    # st.write('ADD MORE DETAILS ABOUT WHAT OUR PROJECT CAN DO')
    st.write('\n\nThis application is a collaboration work of the below mentioned team from IIIT Allahabad.\n\n'
             'It is developed as our **Software Engineering** project. This project deals with the visualisation and '
             'analysis on hepatitis data set. For further information on this application visit the home page '
             '\n\n\n\n**HAVE A NICE DAY :)**\n\n\n\n** Thanks For Visiting** ')
    st.subheader('**TEAM MEMBERS**')

    col1, col2, col3, col4 = st.beta_columns(4)
    col1.image('https://avatars.githubusercontent.com/u/54600270?v=4', width = 250)
    col1.write('Jyotika')
    col1.write('[Github](https://github.com/Jyotika999)')
    col2.image('https://avatars.githubusercontent.com/u/58432166?v=4', width=250)
    col2.write('Vidushi')
    col2.write('[Github](https://github.com/vidushi1012)')
    col3.image('https://avatars.githubusercontent.com/u/58389098?v=4', width=250)
    col3.write('Aarushi')
    col3.write('[Github](https://github.com/shee35)')
    col4.image('https://avatars.githubusercontent.com/u/58399279?v=4', width=250)
    col4.write('Medha')
    col4.write('[Github](https://github.com/medhabalani)')

