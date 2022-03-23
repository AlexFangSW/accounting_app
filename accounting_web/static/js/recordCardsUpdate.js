// Update Modal
async function updateRecord(recordId, crsfToken, data) {
  console.log(`http://127.0.0.1:8000/api/tags/${data.tag_id}/`);
  let formData = new FormData();
  formData.append("income_or_expense", data.type);
  formData.append("tag_name", `http://127.0.0.1:8000/api/tags/${data.tag_id}/`);
  formData.append("discription", data.discription);
  formData.append("price", data.price);
  formData.append("date", data.date);

  let res = await fetch(`http://127.0.0.1:8000/api/records/${recordId}/`, {
    method: "PATCH",
    headers: {
      "X-CSRFToken": crsfToken,
    },
    body: formData,
  });
  console.log(res);
}

function getData(dom) {
  return {
    type: `${dom.querySelector("select option:checked").value}`,
    tag: `${
      dom.querySelector(
        "div[class*=input-group][class*=tags]:not(.d-none) select option:checked"
      ).value
    }`,
    tag_id: `${dom
      .querySelector(
        "div[class*=input-group][class*=tags]:not(.d-none) select option:checked"
      )
      .getAttribute("tag-id")}`,
    discription: `${dom.querySelector("input[name=discription]").value}`,
    price: dom.querySelector("input[name=price]").value,
    date: `${dom.querySelector("input[name=date]").value}`,
  };
}

let recordUpdateModalList = document.querySelectorAll(
  "button.record-card-update"
);
recordUpdateModalList.forEach((element) => {
  element.addEventListener("click", () => {
    const recordId = element.getAttribute("record-id");
    const crsfToken = document
      .querySelector("input[name=csrfmiddlewaretoken]")
      .getAttribute("value");
    const data = getData(document.querySelector(`div.updateModal-${recordId}`));
    console.log(data);
    updateRecord(recordId, crsfToken, data);
  });
});
