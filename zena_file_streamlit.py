import pandas as pd
import streamlit
import snowflake.connector
streamlit.title("Zena's Amazing Catalog")






# connector for snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# snowflake query to get the data of catalog_website view which was created by zena in the last (The big code)
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog=my_cur.fetchall()

catalog_dataframe= pd.DataFrame(my_catalog)


color_list=catalog_dataframe[0].values.tolist()

option_selected= streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))

product_caption= 'Our warm, confortable,' + option_selected+ 'sweatsuit!'


my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + option_selected + "';")


# insert into fruit_load_list values('"+add_my_fruit+"')



df2 = my_cur.fetchone()
streamlit.image(
df2[0],
width=400,
caption= product_caption
)
streamlit.write('Price: ', df2[1])
streamlit.write('Sizes Available: ',df2[2])
streamlit.write(df2[3])





# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)
