import streamlit as st
import plotly.graph_objects as go
import collections

st.set_page_config(layout="wide")
st.title("AVB8 - Sankey Diagram")

data = [
    [ 'Packaged Vials', 'Value', 532.8 ],
    [ 'Samples', 'Waste', 189.5 ],
    [ 'Expired Vials', 'Waste', 611.8 ],
    [ 'Expired DS', 'Waste', 0 ],
    [ 'Filling Loss', 'Waste', 2692.3 ],
    [ 'Rejected DS', 'Waste', 0 ],
    [ 'Inventory Vials', 'Inventory', 979.9 ],
    [ 'Frozen Bulk', 'Inventory', 9309.5 ],
    [ 'AVB8 Run 1', 'DS', 7169.4 ],
    [ 'AVB8 Run 2', 'DS', 7065.9 ],
    [ 'DS', 'Frozen Bulk', 1855.7 ],
    [ 'DS', 'Frozen Bulk', 1296.4 ],
    [ 'DS', 'Frozen Bulk', 1094.8 ],
    [ 'DS', 'Frozen Bulk', 1098 ],
    [ 'DS', 'Frozen Bulk', 1881.1 ],
    [ 'DS', 'Frozen Bulk', 1881.1 ],
    [ 'DS', 'Frozen Bulk', 1854.2 ],
    [ 'DS', 'Frozen Bulk', 1500.3 ],
    [ 'DS', 'Filling', 1854.2 ],
    [ 'Frozen Bulk', 'Filling', 1296.4 ],
    [ 'Frozen Bulk', 'Filling', 1855.7 ],
    [ 'Filling', 'Filling Loss', 955. ],
    [ 'Filling', 'Samples', 52.5 ],
    [ 'Filling', 'Packaged Vials', 202.9 ],
    [ 'Filling', 'Samples', 32 ],
    [ 'Filling', 'Expired Vials', 611.8 ],
    [ 'Filling', 'Filling Loss', 685.8 ],
    [ 'Filling', 'Samples', 52.5 ],
    [ 'Filling', 'Packaged Vials', 0 ],
    [ 'Filling', 'Inventory Vials', 558.1 ],
    [ 'Filling', 'Filling Loss', 1051.5 ],
    [ 'Filling', 'Samples', 52.5 ],
    [ 'Filling', 'Packaged Vials', 54.7 ],
    [ 'Filling', 'Packaged Vials', 82.6 ],
    [ 'Filling', 'Packaged Vials', 192.6 ],
    [ 'Filling', 'Inventory Vials', 421.8 ]
]

# First pass to map steps to index
step_to_index = {}
curr_idx = 0
for u, v, _ in data:
    if u not in step_to_index:
        step_to_index[u] = curr_idx
        curr_idx += 1
    if v not in step_to_index:
        step_to_index[v] = curr_idx
        curr_idx += 1

# Second pass to build sankey data
source = []
target = []
value = []
for u, v, w in data:
    source.append(step_to_index[u])
    target.append(step_to_index[v])
    value.append(w)

label = [None] * len(step_to_index)
for k, v in step_to_index.items():
    label[v] = k

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=10,
        thickness=10,
        line=dict(color="black", width=0.5),
        label=label,
    ),
    link=dict(
        source=source,
        target=target,
        value=value
    ))])

fig.update_layout(
    title_text="AVB8 - Sankey Diagram",
    font_size=16,
    width=1400,
    height=800
)

st.plotly_chart(fig, use_container_width=True)
