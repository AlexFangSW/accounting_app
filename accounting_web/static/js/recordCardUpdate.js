// Update Modal
// async function deleteRecord(recordId, crsfToken) {
//   let res = await fetch(`http://127.0.0.1:8000/api/records/${recordId}/`, {
//     method: 'DELETE',
//     headers: {
//       'X-CSRFToken': crsfToken,
//       'Content-type': 'text/json',
//     },
//   });
//   if (res.ok) {
//     console.log('Delete Success!!');
//     let deletedRecord = document.querySelector(`div[record-id='${recordId}']`);
//     let nextRecord = document.querySelector(
//       `div[record-id='${recordId}']~div[record-id]`
//     );
//     // 拿掉 Deleted element, 然後判斷刪除的是不是這月最上面的
//     if (
//       nextRecord &&
//       deletedRecord.querySelector('div.first_of_month') &&
//       !nextRecord.querySelector('div.first_of_month')
//     ) {
//       // ex: 把 '3月' 補上
//       nextRecord
//         .querySelector('div')
//         .insertBefore(
//           deletedRecord.querySelector('div.first_of_month'),
//           nextRecord.querySelector('div').firstChild
//         );
//     }
//     deletedRecord.remove();
//   } else {
//     console.log('Delete Failed :(');
//   }
// }

// let confirmDeleteList = document.querySelectorAll('button.record-card-update');
// confirmDeleteList.forEach((element) => {
//   const recordId = element.getAttribute('record-id');
//   const crsfToken = document
//     .querySelector('input[name=csrfmiddlewaretoken]')
//     .getAttribute('value');
//   element.addEventListener('click', () => (recordId, crsfToken));
// });
