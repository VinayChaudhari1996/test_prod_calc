import streamlit as st
import streamlit_shadcn_ui as ui


# Define custom CSS style with green color
custom_green = """
<style>
    .title {
        color: #2ECC71; /* Change color to green */
    }
</style>
"""


# Define custom CSS style with green color
custom_red = """
<style>
    .title {
        color: #FF0000; /* Change color to green */
    }
</style>
"""


def calculate_prices(invoice_price, production_cost):
    # Calculate prices
    calc_price_temp = invoice_price * 100
    without_gst_amount = calc_price_temp / 118

    temp_2_price = invoice_price - without_gst_amount
    after_adding_prod_cost = without_gst_amount + production_cost
    profit_10_percentage = after_adding_prod_cost * 0.10
    after_adding_profit_cost = after_adding_prod_cost + profit_10_percentage
    selling_gst_adding = after_adding_profit_cost * 0.18
    selling_final_price = after_adding_profit_cost + selling_gst_adding
    per_kg_selling_price = selling_final_price / 1000
    per_kg_selling_price = round(per_kg_selling_price, 2)

    return {
        "selling_final_price": selling_final_price,
        "per_kg_selling_price": per_kg_selling_price
    }
    

def calculate_prices__without_gst(invoice_price, production_cost):
    
    #B1 = invoice_price
    #B3 = production_cost
    
    #=B1*18%
    gst_of_invoice_price = invoice_price * 0.18

    #=B1+B3
    invoice_price__sum__production_cost = invoice_price + production_cost
    
    #B4 * 10%
    profit_10 = invoice_price__sum__production_cost * 0.10
    
    #=B4+B5
    profit_10__sum__production = invoice_price__sum__production_cost + profit_10
    
    adding_gst = profit_10__sum__production * 0.18
    
    selling_price = profit_10__sum__production + adding_gst
    
    per_kg_price = selling_price / 1000
    per_kg_price = round(per_kg_price, 2)

    
    
    return {
        "selling_final_price": selling_price,
        "per_kg_selling_price": per_kg_price
    }

def main():
    # st.markdown(custom_green, unsafe_allow_html=True)
    
    st.markdown("### Ingot Selling Calculator with GST")
    
    # Input boxes
    invoice_price = st.number_input("Invoice price of scrape", value=0, key="main_invoice_price")
    production_cost = st.number_input("Production cost", value=0, key="main_production_cost")
    
    if ui.button(text="Submit", key="styled_btn_tailwind", className="bg-green-500 text-white"):
        # Calculate prices
        results = calculate_prices(invoice_price, production_cost)
        
        # Show results in card
        st.markdown("#### Final Prices")
        
        temp_1 = results["selling_final_price"]
        temp_2 = results["per_kg_selling_price"]
        
        cols = st.columns(2)
        with cols[0]:
            ui.metric_card(title="Selling Final Price", content=temp_1, description="", key="card1_main")
        with cols[1]:
            ui.metric_card(title="Per KG Selling Price", content=temp_2, description="", key="card2_main")




def test_main():
    st.markdown("___")

    st.markdown(custom_red, unsafe_allow_html=True)
    st.markdown("<h3 class='title'>Without GST Calculator</h3>", unsafe_allow_html=True)
    
    
    # Input boxes
    invoice_price = st.number_input("Invoice price of scrape", value=0, key="test_invoice_price")
    production_cost = st.number_input("Production cost", value=0, key="test_production_cost")
    
    if ui.button(text="Submit", key="styled_btn_tailwind_test", className="bg-red-500 text-white"):
        # Calculate prices
        results = calculate_prices__without_gst(invoice_price, production_cost)
        
        # Show results in card
        st.markdown("#### Test Final Prices")
        
        temp_1 = results["selling_final_price"]
        temp_2 = results["per_kg_selling_price"]
        
        cols = st.columns(2)
        with cols[0]:
            ui.metric_card(title="Test Selling Final Price", content=temp_1, description="", key="card1_test")
        with cols[1]:
            ui.metric_card(title="Test Per KG Selling Price", content=temp_2, description="", key="card2_test")

if __name__ == "__main__":
    main()
    test_main()
