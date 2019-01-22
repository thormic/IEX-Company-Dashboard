% rebase('base.tpl', title='Python')

<form action="/note_added" method="post">
<div class="container" style="width: 1600px; height: 750px">
    <div class="row">
        <div class="col-lg-12 d-flex align-items-stretch" style=" height: auto" >
            <div class="card border-primary mb-2" style="padding: 100px">
                <h1 style="text-align: center">Add your note for {{!company}}</h1>
                <div class="form-group">
                    <label for="exampleFormControlTextarea" style="font-size: large">Note:</label>
                        <textarea class="form-control"
                            name="note"
                            id="exampleFormControlTextarea"
                            style="font-size: medium"
                            rows="3">
                        </textarea>
                </div>
                <div class="form-check" style="padding: 15px 0px 0px 20px">
                    <input value="submit" type="submit">
                </div>
            </div>
        </div>
    </div>
</div>
