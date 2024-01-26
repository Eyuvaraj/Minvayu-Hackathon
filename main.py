import streamlit as st
from streamlit_extras.streaming_write import write
from streamlit_chat import message
import matplotlib.pyplot as plt
import numpy as np

from Gemini import model

st.set_page_config(
    page_title="House Builder",
    layout="wide",
    page_icon="🏠",
    menu_items=None,
)

with st.container():
    st.title("House Builder")
    st.subheader("Builds a 3d Model of a House from your description")
    st.divider()


def main():
    room_length = st.text_input("Room Length (in meters):")
    room_width = st.text_input("Room Width (in meters):")
    room_height = st.text_input("Room Height (in meters):")

    windows_count = st.number_input(
        "Number of Windows:", min_value=0, max_value=8, value=0
    )
    doors_count = st.number_input("Number of Doors:", min_value=0, max_value=4, value=0)

    if st.button("Generate 3D Model"):
        room_info = {
            "Length": room_length,
            "Width": room_width,
            "Height": room_height,
            "Windows": windows_count,
            "Doors": doors_count,
        }

        chat = model.start_chat(history=[])

        prompt = generate_prompt(room_info)

        response = chat.send_message(prompt)

        with st.spinner("Generating response..."):
            st.chat_message("Gemini")
            write_gemini_response(response.text)
        canvas_image = generate_canvas_image(room_info)
        st.image(canvas_image, caption="Generated Canvas Image", use_column_width=True)

        # Read Gemini response from file and display
        gemini_response = read_gemini_response()
        st.text("Gemini Response:")
        st.text(gemini_response)


def generate_prompt(room_info):
    prompt = (
        f"Generate a 3D CAD model code for a room with the following specifications:\n"
    )
    prompt += f"Length: {room_info['Length']} meters\n"
    prompt += f"Width: {room_info['Width']} meters\n"
    prompt += f"Height: {room_info['Height']} meters\n"
    prompt += f"Number of Windows: {room_info['Windows']}\n"
    prompt += f"Number of Doors: {room_info['Doors']}\n"
    return prompt


def write_gemini_response(response):
    with open("gemini_response.txt", "w") as file:
        file.write(response)


def read_gemini_response():
    with open("gemini_response.txt", "r") as file:
        return file.read()


def generate_canvas_image(room_info):
    # Assuming you have the logic to generate a canvas image based on room_info
    # Modify this function according to your requirements
    # Example: Creating a simple placeholder canvas image
    canvas_image = np.zeros((100, 100, 3), dtype=np.uint8)
    canvas_image.fill(255)  # White canvas
    return canvas_image


if __name__ == "__main__":
    main()
