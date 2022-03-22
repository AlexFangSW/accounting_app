// 預設為今天
document.querySelector('input.datetimepicker-input').valueAsDate = new Date();
// 一次只顯示一種tag (支出、收入)
let addInputGoupList = document.querySelectorAll('div.addInputGroup');

addInputGoupList.forEach((element) => {
  let selector = element.querySelector('select.income_or_expense');

  let income_tag = element.querySelector('div.tags-income select');
  let expense_tag = element.querySelector('div.tags-expense select');
  let expense_tag_input = element.querySelector('div.input-group.tags-expense');
  let income_tag_input = element.querySelector('div.input-group.tags-income');

  selector.addEventListener('click', () => {
    let current_select = selector.querySelector('option:checked').value;
    if (current_select == '支出') {
      expense_tag.setAttribute('name', 'tag_name');
      expense_tag_input.classList.remove('d-none');
      income_tag.setAttribute('name', '');
      income_tag_input.classList.add('d-none');
    } else {
      expense_tag.setAttribute('name', '');
      expense_tag_input.classList.add('d-none');
      income_tag.setAttribute('name', 'tag_name');
      income_tag_input.classList.remove('d-none');
    }
  });
});
