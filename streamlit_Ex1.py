import streamlit as st
import pandas as pd

st.title('Hello Streamlit!')
st.write("This is my first Streamlit app.")

st.header('Header Example')
st.subheader('Subheader Example')
st.text('This is a simple text example.')
st.markdown('This is a **Markdown** example with *italic* and **bold** text.')
st.code('print("Hello, World!")', language='python')
st.image('https://via.placeholder.com/150', caption='Sample Image')
st.video('https://www.youtube.com/watch?v=ZhcX07Quti8')
st.button('Click Me', on_click=lambda: st.write('Button clicked!'))
st.checkbox('Check me!', value=True)
st.radio('Choose an option:', options=['Option 1', 'Option 2', 'Option 3'])
st.selectbox('Select a fruit:', options=['Apple', 'Banana', 'Cherry'])
st.multiselect('Select multiple fruits:', options=['Apple', 'Banana', 'Cherry'])
st.slider('Select a number:', min_value=0, max_value=100, value=50)
st.text_input('Enter your name:', placeholder='Type here...')
st.text_area('Enter your message:', placeholder='Type your message here...')
st.date_input('Select a date:')
st.time_input('Select a time:')
st.file_uploader('Upload a file:', type=['txt', 'pdf', 'png', 'jpg'])
st.progress(50)  # Display a progress bar at 50%
st.spinner('Loading...')  # Show a spinner while loading
st.sidebar.title('Sidebar Example')
st.sidebar.write('This is a sidebar example.')
st.sidebar.checkbox('Sidebar Checkbox', value=True)
st.sidebar.selectbox('Sidebar Selectbox:', options=['Option A', 'Option B'])
st.sidebar.slider('Sidebar Slider:', min_value=0, max_value=100, value=25)
st.balloons()  # Show balloons animation
st.success('This is a success message!')

# Example DataFrame
pd = pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': ['A', 'B', 'C'],
    'Column 3': [True, False, True]
})
st.dataframe(pd)  # Display DataFrame in the app

st.table(pd)  # Display DataFrame as a static table
st.json({'key': 'value', 'number': 42, 'boolean': True})  # Display JSON data
st.markdown('''
## Markdown Example
This is an example of a **Markdown** section with a list:
- Item 1
- Item 2
- Item 3                    
''')
st.write('''
## Additional Features
- Use `st.write()` for general text and data display.
- Use `st.markdown()` for formatted text.
- Use `st.code()` for displaying code snippets.
- Use `st.image()` to display images.
- Use `st.video()` to embed videos.
- Use `st.button()` for interactive buttons.
- Use `st.checkbox()` for checkboxes.
- Use `st.radio()` for radio buttons.
- Use `st.selectbox()` for dropdown selections.
- Use `st.multiselect()` for multiple selections.
- Use `st.slider()` for sliders.
- Use `st.text_input()` for single-line text input.
- Use `st.text_area()` for multi-line text input.
- Use `st.date_input()` for date selection.
- Use `st.time_input()` for time selection.
- Use `st.file_uploader()` for file uploads.
- Use `st.progress()` for progress bars.
- Use `st.spinner()` to show a loading spinner.
''')