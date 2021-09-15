import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

data = pd.read_csv(r"C:\Users\Clarisa Hilario\Documents\YR3TERM3\DATANVI\project\ds\updated1.csv")

app = dash.Dash(__name__)
# exp list
exp = ['Total Food Expenditure',
       'Restaurant and hotels Expenditure',
       'Alcoholic Beverages Expenditure',
       'Tobacco Expenditure',
       'Clothing, Footwear and Other Wear Expenditure',
       'Housing and water Expenditure', 'Medical Care Expenditure',
       'Transportation Expenditure',
       'Communication Expenditure',
       'Education Expenditure',
       'Miscellaneous Goods and Services Expenditure',
       'Special Occasions Expenditure',
       'Crop Farming and Gardening expenses']

# average net income per region dataframe
ave_net = data.groupby('Region', as_index=False)['net_hincome'].mean()
ave_net = ave_net.rename(columns={"net_hincome": "ave_net"}, errors="raise")
# ave total income
ave_income = data.groupby('Region', as_index=False)['Total Household Income'].mean()
ave_income = ave_income.rename(columns={"Total Household Income": "ave_income"}, errors="raise")
# 1st set radio buttons
rset1_list = ['Average Total Income', 'Average Net Income']
rset1 = []
for i in rset1_list:
    rset1.append({
        "label": i,
        "value": i
    })
rset2_list = ['Select per Region', 'Select per Factor']
rset2 = []
for i in rset2_list:
    rset2.append({
        "label": i,
        "value": i
    })

# get dropdown lists
regions = []
region_list = sorted(data['Region'].unique())
for i in region_list:
    regions.append({
        "label": i,
        "value": i
    })

factors_list = ['Main Source of Income', 'Household head age and sex',
                'Household head marital status', 'Household head occupation',
                'Number of Household members']
factors = []
for i in factors_list:
    factors.append({
        "label": i,
        "value": i
    })
# app layout
app.layout = html.Div(className='container', children=[
    html.Div(className="row", children=[
        html.Div(className="col-12", children=[
            html.H1('Regional analysis of Filipino Family Income and Expenditure'),
            html.P(
                'The socio-economic classification (SEC) has been used to determine the collective stability and security of the nation. This is broken down into three groups such as low, middle and high and are usually assessed by the nation’s income, education and occupation. The Philippines have set different goals such as lowering the unemployment rate, decreasing poverty incidence, maintaining economic growth and many more in order to attain a higher classification. The report for economic growth usually lies on the overall improvement or deterioration of the country in relation to the goals to be achieved. Economic analysts have argued that the reported  socio-economic growth in the Philippines is not a reliable indicator for SEC as most of the reports come from regions composed of developed cities and do not consider factors such as expenditure versus income or give focus to rural regions and their conditions. The goal is to determine the socio-economic conditions per region and the factors that contribute to it such as income and occupation.')
        ])
    ]),
    # radio buttons 1
    html.Div(className="row", children=[
        html.Div(className="col-7", children=[
            dcc.RadioItems(
                id="rchoice1",
                options=rset1,
                value='Average Total Income'
            )
        ])
    ]),
    # bar chart
    html.Div(className="row", children=[
        html.Div(className="col-11", children=[
            dcc.Graph(
                id="cresult1"
            )
        ])
    ]),
    html.Div(className="row", children=[
        html.Div(className="col-11", children=[
            html.Div(
                id="1-graph-analysis"
            ),
            html.H4('Analysis of Factors affecting SEC per region'),
            html.P(
                'To see further see what the socio-economic condition per region, we will explore the different factors that influences the total income per household as well as their net income. It would show the different trends and relationships of these factors')
        ])
    ]),
    # radio buttons 2
    html.Div(className="row", children=[
        html.Div(className="col-7", children=[
            dcc.Dropdown(
                id="region-dd",
                options=regions
            )
        ])
    ]),
    html.Div(className="row", children=[
        html.Div(className="col-12", children=[
            dcc.Graph(
                id="main-source-graph"
            )
        ])
    ]),
    html.Div(className="row", children=[
        html.Div(className="col-12", children=[
            html.Div(
                id="ms-analysis"
            )
        ])
    ]),
    html.Div(className="row", children=[
        html.Div(className="col-14", children=[
            dcc.Graph(
                id="occ-graph"
            )
        ])
    ]),
    html.Div(className="row", children=[
        html.Div(className="col-14", children=[
            html.Div(
                id="occ-analysis"
            )
        ])
    ]),
    html.Div(className="row", children=[
        html.Div(className="col-10", children=[
            dcc.Graph(
                id="status-graph"
            )
        ])
    ]),
    html.Div(className="row", children=[
        html.Div(className="col-10", children=[
            html.Div(
                id="status-analysis"
            )
        ])
    ]),
    html.Div(className="row", children=[
        html.Div(className="col-10", children=[
            dcc.Graph(
                id="te-num-graph"
            )
        ])
    ]),
    html.Div(className="row", children=[
        html.Div(className="col-10", children=[
            html.Div(
                id='numexp-analysis'
            )
        ])
    ]),
    html.Div(className="row", children=[
        html.Div(className="col-10", children=[
            dcc.Graph(
                id="age-sex-graph"
            )
        ])
    ]),
    html.Div(className="row", children=[
        html.Div(className="col-10", children=[
            html.Div(
                id="agesex-analysis"
            )
        ])
    ])
])


# call back for radioitems 1
@app.callback(
    # id, propoerty
    Output('cresult1', 'figure'),
    Output('1-graph-analysis', 'children'),
    Input('rchoice1', 'value')
)
# def for radio button result 1
def ave_income_graph(radio_choice1):
    global fig, analysis
    if 'Average Total Income' == radio_choice1:
        fig = px.bar(ave_income, x="ave_income", y="Region", orientation="h", title="Average Total Income per Region")
        fig.update_layout(transition_duration=1000, title="Average Total Income per Region")
        analysis = 'The bar chart shows the Average total income of all households within each region with NCR having the highest average total income among the regions and ARMM having the lowest average total income.'
    elif 'Average Net Income' == radio_choice1:
        fig = px.bar(ave_net, x="ave_net", y="Region", orientation="h", title="Average Net Income per Region")
        fig.update_layout(transition_duration=1000, title="Average Net Income per Region")
        analysis = 'The net income can be computed by subtracting all expenditures from the total income. The average of the net income of all regions is then shown. Observe that ARMM has a negative average net income which may indicate that the income per household is not sufficient in supporting the annual needs of the household.'
    return fig, analysis


# callback input: region-dd; outputs: selected charts
@app.callback(
    Output('main-source-graph', 'figure'),  # main source
    Output('ms-analysis', 'children'),
    Output('occ-graph', 'figure'),  # head occupation
    Output('occ-analysis', 'children'),
    Output('status-graph', 'figure'),  # marital status
    Output('status-analysis', 'children'),
    Output('te-num-graph', 'figure'),  # total exp vs num members
    Output('numexp-analysis', 'children'),
    Output('age-sex-graph', 'figure'),  # age and sex
    Output('agesex-analysis', 'children'),
    Input('region-dd', 'value')
)
def update_mainsource_graph(region):
    filt_data = data.loc[data['Region'] == region]
    # main source
    sources = filt_data['Main Source of Income'].value_counts().rename_axis('Main Sources').reset_index(name='counts')
    fig1 = px.pie(sources, values='counts', names='Main Sources', title='Main Sources of Income in ' + region)
    fig1.update_layout(transition_duration=1000, title="Main Sources of Income in " + region)

    # main source analysis
    ms_majority = sources['Main Sources'][0]
    ms_minority = sources['Main Sources'][len(sources) - 1]
    ms_analysis = 'In the ' + region + ' , majority of the main sources of income are ' + ms_majority + 'while the ' \
                                                                                                        'minority get ' \
                                                                                                        'their income ' \
                                                                                                        'from ' + \
                  ms_minority + '. '

    # head occ
    occ = filt_data['Household Head Occupation'].value_counts().rename_axis('Head Occupation').reset_index(
        name='counts')
    occ = occ.nlargest(100, 'counts')
    occ_mean = occ['counts'].mean()
    occ = occ.drop(occ[occ.counts < occ_mean].index)
    fig2 = px.bar(occ, x="counts", y="Head Occupation", orientation="h",
                  title="Top Household Head Occupation in " + region)
    fig2.update_layout(transition_duration=1000, title="Top Household Head Occupation in " + region)

    # occ analysis
    occ_max = occ['counts'].idxmax()
    occ_majority = occ['Head Occupation'][occ_max]
    occ_analysis = 'The graph shows the list of household head occupations that are above the mean count for each ' \
                   'unique occupation. Majority of household heads have the occupation of ' + occ_majority + ' in ' + \
                   region + '. '

    # marital status
    status = filt_data['Household Head Marital Status'].value_counts().rename_axis('Marital Status').reset_index(
        name='counts')
    fig3 = px.pie(status, values='counts', names='Marital Status', title='Household Head Marital Status in ' + region)
    fig3.update_layout(transition_duration=1000, title="Household Head Marital Status in " + region)

    # status analysis
    stat_max = status['counts'].idxmax()
    stat_min = status['counts'].idxmin()
    stat_minority = status['Marital Status'][stat_min]
    stat_majority = status['Marital Status'][stat_max]
    stat_analysis = 'Majority of the household heads in ' + region + ' has a marital status of ' + stat_majority + '.'

    # # of members vs expenditures
    fig4 = px.violin(filt_data, x="Total Number of Family members", y="total_expenditures",
                     title="Total Expenditures vs Number of Household members in " + region)
    fig4.update_layout(transition_duration=1000, title="Total Expenditures vs Number of Household members in " + region)

    # num vs exp analysis
    exp_id = filt_data['total_expenditures'].idxmax()
    exp_max = str(filt_data['total_expenditures'][exp_id])
    num_max = str(filt_data['Total Number of Family members'][exp_id])
    numexp_analysis = 'In ' + region + ', the highest total expenditures of ' + exp_max + ' houses a total of ' + num_max + ' members.'

    # age & sex
    fig5 = px.histogram(filt_data, x="Household Head Age", color="Household Head Sex",
                        title="Household Head Age and Sex in " + region)
    fig5.update_layout(transition_duration=1000, title="Household Head Age and Sex in " + region)

    # age and sex analysis
    sex = filt_data['Household Head Sex'].value_counts().rename_axis('Household Head Sex').reset_index(name='counts')
    sex_max = sex['counts'].idxmax()
    sex_majority = sex['Household Head Sex'][sex_max]
    numsex = filt_data.groupby(['Household Head Sex', 'Household Head Age']).size().reset_index(name='counts')
    filt_numsex = numsex.loc[numsex['Household Head Sex'] == sex_majority]
    filtsex_age_max = filt_numsex['counts'].idxmax()
    age_majority = str(filt_numsex['Household Head Age'][filtsex_age_max])
    agesex_analysis = 'The sex of majority of the household heads in ' + region + ' are ' + sex_majority + 'in which majority ' \
                                                                                                           'of them are of ' \
                                                                                                           'the age ' \
                                                                                                           '' + age_majority + '. '

    return fig1, ms_analysis, fig2, occ_analysis, fig3, stat_analysis, fig4, numexp_analysis, fig5, agesex_analysis


if __name__ == '__main__':
    app.run_server()
