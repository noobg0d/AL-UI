import streamlit as st
import pandas as pd
import comparekmplgraphss as ckg
import compare_kmpl2vin as ckt
import comparekmplgraph4 as ckp


def main():
    st.title(":articulated_lorry: KMPL Comparison ")
    num_vehicles = st.selectbox("Select the number of vehicles:", [2, 3, 4])
    st.write(f"You have compared: {num_vehicles} vehicles")
    if num_vehicles==4:
    # Add file uploader for multiple files
        uploaded_files1 = st.file_uploader("Upload files for vehicle 1", type=["csv", "xlsx"], accept_multiple_files=True)
        uploaded_files2 = st.file_uploader("Uploaded files for vehicle 2", type=["csv", "xlsx"], accept_multiple_files=True)
        uploaded_files3 = st.file_uploader("Upload files for vehicle 3", type=["csv", "xlsx"], accept_multiple_files=True)
        uploaded_files4 = st.file_uploader("Upload files for vehicle 4", type=["csv", "xlsx"], accept_multiple_files=True)
        ## for first files
        if uploaded_files1:
            for uploaded_file in uploaded_files1:
                df1 = pd.read_csv(uploaded_file)
        # for second file
        if uploaded_files2:
            for uploaded_file in uploaded_files2:
                df2 = pd.read_csv(uploaded_file)
            # for third file
        if uploaded_files3:
            for uploaded_file in uploaded_files3:
                df3 = pd.read_csv(uploaded_file)
        # for fourth file 
        if uploaded_files4:
            for uploaded_file in uploaded_files4:
                df4 = pd.read_csv(uploaded_file)
            ckp.plot_graphs(df1,df2,df3,df4)
            st.title('Download Merged PDF')
            st.markdown("Click the button below to download the merged PDF.")

            # Function to download the merged PDF
            def download_merged_pdf():
                with open('merged_plots.pdf', 'rb') as pdf_file:
                    pdf_bytes = pdf_file.read()
                st.download_button(label='Download Merged PDF', data=pdf_bytes, file_name='merged_plots.pdf', key='download_pdf')
            
            # Display the download button
            download_merged_pdf()
            
            # for 3 vehicles
    elif num_vehicles==3:
        uploaded_files1 = st.file_uploader("Upload files for vehicle 1", type=["csv", "xlsx"], accept_multiple_files=True)
        uploaded_files2 = st.file_uploader("Uploaded files for vehicle 2", type=["csv", "xlsx"], accept_multiple_files=True)
        uploaded_files3 = st.file_uploader("Upload files for vehicle 3", type=["csv", "xlsx"], accept_multiple_files=True)
        ## for first files
        if uploaded_files1:
            for uploaded_file in uploaded_files1:
                df1 = pd.read_csv(uploaded_file)
        # for second file
        if uploaded_files2:
            for uploaded_file in uploaded_files2:
                df2 = pd.read_csv(uploaded_file)
            # for third file
        if uploaded_files3:
            for uploaded_file in uploaded_files3:
                df3 = pd.read_csv(uploaded_file)
                
        if uploaded_files1 and uploaded_files2 and uploaded_files3:
            ckt.plot_graphs(df1, df2, df3)
            
            
            st.title('Download Merged PDF')
            st.markdown("Click the button below to download the merged PDF.")

            # Function to download the merged PDF
            def download_merged_pdf():
                with open('merged_plots.pdf', 'rb') as pdf_file:
                    pdf_bytes = pdf_file.read()
                st.download_button(label='Download Merged PDF', data=pdf_bytes, file_name='merged_plots.pdf', key='download_pdf')
            
            # Display the download button
            download_merged_pdf()
            
    else:
        uploaded_files1 = st.file_uploader("Upload files for vehicle 1", type=["csv", "xlsx"], accept_multiple_files=True)
        uploaded_files2 = st.file_uploader("Uploaded files for vehicle 2", type=["csv", "xlsx"], accept_multiple_files=True)
        if uploaded_files1:
            for uploaded_file in uploaded_files1:
                df1 = pd.read_csv(uploaded_file)
        # for second file
        if uploaded_files2:
            for uploaded_file in uploaded_files2:
                df2 = pd.read_csv(uploaded_file)
        
        if uploaded_files1 and uploaded_files2:
            ckg.plot_graphs(df1,df2)
            # Display the download button
            st.title('Download Merged PDF')
            st.markdown("Click the button below to download the merged PDF.")

            # Function to download the merged PDF
            def download_merged_pdf():
                with open('merged_plots.pdf', 'rb') as pdf_file:
                    pdf_bytes = pdf_file.read()
                st.download_button(label='Download Merged PDF', data=pdf_bytes, file_name='merged_plots.pdf', key='download_pdf')
            
            # Display the download button
            download_merged_pdf()
            

if __name__ == "__main__":
    main()
    
    

