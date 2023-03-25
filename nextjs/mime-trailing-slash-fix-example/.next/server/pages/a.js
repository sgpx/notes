"use strict";
(() => {
var exports = {};
exports.id = 9;
exports.ids = [9];
exports.modules = {

/***/ 678:
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__),
/* harmony export */   "getServerSideProps": () => (/* binding */ getServerSideProps)
/* harmony export */ });
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(997);
/* harmony import */ var react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__);

const refData = Array(100).fill(0).map((_, n)=>({
        id: n,
        text: `item ${n} :  ${Math.random() * Math.pow(10, 6)}`
    }));
const HomePage = ({ data , nkey , pkey  })=>/*#__PURE__*/ (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)(react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.Fragment, {
        children: [
            pkey !== null ? /*#__PURE__*/ react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx("a", {
                href: `?n=${pkey}`,
                children: "prev"
            }) : null,
            data.map((x)=>/*#__PURE__*/ (0,react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxs)("div", {
                    children: [
                        x.id,
                        " - ",
                        x.text
                    ]
                }, x.id)),
            nkey !== null ? /*#__PURE__*/ react_jsx_runtime__WEBPACK_IMPORTED_MODULE_0__.jsx("a", {
                href: `?n=${nkey}`,
                children: "next"
            }) : null
        ]
    });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (HomePage);
async function getServerSideProps(ctx) {
    const a = ctx?.query?.n;
    const i = a ? parseInt(a) : 0;
    const pkey = i > 0 ? i - 10 : null;
    const nkey = i < refData.length - 10 ? i + 10 : null;
    console.log(i, i + 10);
    const dataSlice = refData.slice(i, i + 10);
    return {
        props: {
            data: dataSlice,
            nkey,
            pkey
        }
    };
}


/***/ }),

/***/ 997:
/***/ ((module) => {

module.exports = require("react/jsx-runtime");

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../webpack-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = (__webpack_exec__(678));
module.exports = __webpack_exports__;

})();