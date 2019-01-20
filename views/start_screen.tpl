% rebase('base.tpl', title='Python')

<form action="/main_dashboard" method="post">
<div class="container-fluid" style="height: 750px">
    <div class="row">
        <div class="col-lg-12">
            <h1 style="text-align: center">Select desired company</h1>
        </div>
    </div>
    <div class="row">
        <div class="col-lg-2"></div>
        <div class="col-lg-8">
            <select class="custom-select custom-select-lg mb-3" name="company" style="text-align: center">
            <option selected>Select company</option>
            % for company in companies:
            <option value="{{company}}" style="color: black">{{company}}</option>
            % end
            </select>
        </div>
        <div class="col-lg-2"></div>
    </div>
    <div class="row">
        <div class="col-lg-2"></div>
        <div class="col-lg-8" style="text-align: center">
        Start:<input name="start_date" type="text" placeholder="YYYY-MM-DD">
        End:<input name="end_date" type="text" placeholder="YYYY-MM-DD">
        </div>
        <div class="col-lg-2"></div>
    </div>
    <div class="row">
        <div class="col-lg-2"></div>
        <div class="col-lg-8" style="text-align: center">
            <div class="form-check" style="padding: 15px 0px 0px 20px">
                <input value="submit" type="submit">
            </div>
        </div>
        <div class="col-lg-2"></div>
    </div>
</div>
</form>
