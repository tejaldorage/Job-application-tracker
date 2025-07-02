from flask import Flask, render_template, request, redirect, url_for, session, flash
import pandas as pd, os

app = Flask(__name__)
app.secret_key = 'replace_with_secure_key'
EXCEL = 'applications.xlsx'
if not os.path.exists(EXCEL):
    pd.DataFrame(columns=['Application ID','Company Name','Job Title','Status']).to_excel(EXCEL,index=False)

def read_df(): return pd.read_excel(EXCEL)
def write_df(df): df.to_excel(EXCEL,index=False)

@app.route('/')
def home():
    df = read_df()
    return render_template('home.html', stats=df['Status'].value_counts().to_dict())

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        df = read_df()
        # Option A: using concat
        new_row = pd.DataFrame([{
            'Application ID': request.form['id'],
            'Company Name': request.form['company'],
            'Job Title': request.form['title'],
            'Status': request.form['status']
        }])
        df = pd.concat([df, new_row], ignore_index=True)

        write_df(df)
        return redirect(url_for('list_apps'))
    return render_template('add.html')
    

@app.route('/edit/<app_id>', methods=['GET', 'POST'])
def edit(app_id):
    df = read_df()
    df['ID_str'] = df['Application ID'].astype(str)
    
    if request.method == 'POST':
        selected = request.form.get('id')
        if isinstance(selected, list):
            selected = selected[0]
        mask = df['ID_str'] == selected
        if not mask.any():
            flash(f"No application found with ID {selected}", "warning")
            return redirect(url_for('list_apps'))
        
        # update
        df.loc[mask, ['Company Name', 'Job Title', 'Status']] = [
            request.form['company'], request.form['title'], request.form['status']
        ]
        write_df(df.drop(columns='ID_str'))
        return redirect(url_for('list_apps'))

    # GET case: load row for form
    mask = df['ID_str'] == str(app_id)
    if not mask.any():
        flash(f"No application found with ID {app_id}", "warning")
        return redirect(url_for('list_apps'))
    row = df[mask].iloc[0].to_dict()
    return render_template('edit.html', app=row)

import os
print("Path:", os.path.abspath(EXCEL))
print("Exists:", os.path.exists(EXCEL))
print("Is file?", os.path.isfile(EXCEL))

@app.route("/delete/<app_id>", methods=["POST"])
def delete(app_id):
    df = read_df()
    new_df = df[df["Application ID"] != app_id]
    write_df(new_df)  # uses to_excel or ExcelWriter
    return redirect(url_for("list_apps"))

@app.route('/list')
def list_apps():
    return render_template('list.html', apps=read_df().to_dict(orient='records'))


@app.route('/track', methods=['GET', 'POST'])
def track():
    df = read_df()
    apps_list = df['Application ID'].astype(str).tolist()  # all as strings

    selected = None
    result_app = None
    if request.method == 'POST':
        selected = request.form.get('id')
        # Guarantee it's a string scalar
        if isinstance(selected, list):
            selected = selected[0]
        if selected in apps_list:
            result_app = df[df['Application ID'].astype(str) == selected].iloc[0].to_dict()
        else:
            flash(f"No application found with ID {selected}", "danger")

    return render_template('track.html',
                           apps_list=apps_list,
                           selected=selected,
                           app=result_app)

    
@app.route('/admin', methods=['GET','POST'])
def admin():
    if request.method=='POST':
        if request.form['user']=='admin' and request.form['pass']=='password':
            session['admin']=True
            return redirect(url_for('home'))
        flash('Invalid login')
    return render_template('admin.html')
@app.route('/logout')
def logout():
    session.pop('admin', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)
